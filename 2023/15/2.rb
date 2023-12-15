def calculate_hash(string)
  hash = 0
  ascii_codes = string.codepoints
  for ascii_code in ascii_codes
    hash = hash + ascii_code
    hash = hash * 17
    hash = hash % 256
  end
  return hash
end

def apply_operation_on_box(box, operation, focusing_power, label)
  if operation == "="
    index = box["lenses"].find_index { |lens| lens["label"] == label }
    if index != nil
      box["lenses"][index]["focusing_power"] = focusing_power
    else
      box["lenses"].push({"label" => label, "focusing_power" => focusing_power })
    end
  elsif operation == "-"
    index = box["lenses"].find_index { |lens| lens["label"] == label }
    if index != nil
      box["lenses"].delete_at(index)
    end
  else
    raise "pathetic"
  end
  return box
end

def solve(file_path)
  all_boxes = []

  for i in 0..255
    all_boxes[i] = { "lenses" => [] }
  end

  initialization_sequence = File.open(file_path).read()
  all_steps = initialization_sequence.split(',')

  for current_step in all_steps
    label = current_step.include?("=") ? current_step[0..-3] : current_step[0..-2]
    operation = current_step.include?("=") ? current_step[-2] : current_step[-1]
    focusing_power = current_step.include?("=") ? current_step[-1] : nil
    label_hash = calculate_hash(label)
    current_box = all_boxes[label_hash]
    updated_box = apply_operation_on_box(current_box, operation, focusing_power, label)
    all_boxes[label_hash] = updated_box
  end

  total_focusing_power = 0
  all_boxes.each_with_index do |current_box, index|
    focusing_power_of_current_box = 0
    current_box["lenses"].each_with_index do |lens, lens_index|
      focusing_power_of_current_box += (index + 1) * (lens_index + 1) * lens["focusing_power"].to_i
    end
    total_focusing_power += focusing_power_of_current_box
  end

  print("[#{file_path}]: #{total_focusing_power}\n")
end

solve("sample-2.txt")
solve("input.txt")
