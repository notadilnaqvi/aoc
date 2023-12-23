def parse_workflow(workflow_str)
  name = workflow_str.split("{")[0]

  fallback = workflow_str.split("{")[1].tr("{}", "").split(",")[-1]

  conditions = []

  workflow_str.split("{")[1].tr("{}", "").split(",").each do |condition_str|
    next if condition_str == fallback

    operator = condition_str.split(":")[0].include?(">") ? ">" : "<"

    category = condition_str.split(":")[0].split(operator)[0]
    threshold = condition_str.split(":")[0].split(operator)[1].to_i

    send_to = condition_str.split(":")[1]

    apply = Proc.new { |part| operator == "<" ? part[category] < threshold : part[category] >  threshold }
    conditions.push({
      "apply" => apply,
      "send_to" => send_to
    })
  end

  return {
    "name" => name,
    "conditions" => conditions,
    "fallback" => fallback
  }
end

def parse_part(part_str)
  part = {}
  part_str.tr("{}", "").split(",").each { |rule_str| k, v = rule_str.split("="); part[k] = v.to_i}
  part["rating_sum"] = part["x"] +  part["m"] +  part["a"] +  part["s"]
  return part
end

def solve(file_path)
  file = File.open(file_path).read()

  parts = file.split("\n\n")[1].split("\n").map { |part_str| parse_part(part_str)}

  workflows = file.split("\n\n")[0].split("\n").map { |workflow_str| parse_workflow(workflow_str) }

  starting_workflow = workflows.filter { |workflow| workflow["name"] == "in" }[0]

  total_rating_sum_of_acceped_parts = 0
  for part in parts
    send_to = nil
    current_workflow = starting_workflow
    while send_to != "A" and send_to != "R"
      no_condition_passed = true
      for condition in current_workflow["conditions"]
        if condition["apply"].call(part)
          send_to = condition["send_to"]
          current_workflow = workflows.filter { |workflow| workflow["name"] == send_to }[0]
          no_condition_passed = false
          break
        end
      end
      if no_condition_passed
        send_to = current_workflow["fallback"]
        current_workflow = workflows.filter { |workflow| workflow["name"] == send_to }[0]
      end
    end
    if send_to == "A"
      total_rating_sum_of_acceped_parts += part["rating_sum"]
    end
  end

  print("[#{file_path}]: #{total_rating_sum_of_acceped_parts}\n")
end

solve('sample.txt')
solve('input.txt')
