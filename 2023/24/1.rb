require 'bigdecimal'

LIMITS = {
  "sample.txt" => {"MIN" => BigDecimal("7"), "MAX" => BigDecimal("27") },
  "input.txt" => {"MIN" => BigDecimal("200000000000000"), "MAX" => BigDecimal("400000000000000") },
}

# https://en.wikipedia.org/wiki/Cramer%27s_rule
def solve_linear_equations(eq1, eq2)
  a1 = eq1["a"]
  b1 = eq1["b"]
  c1 = eq1["c"]

  a2 = eq2["a"]
  b2 = eq2["b"]
  c2 = eq2["c"]

  # No solution
  if a1 * b2 - b1 * a2 == BigDecimal("0")
    return nil
  end

  t1 = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
  t2 = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))

  return [t1, t2]
end

def solve(file_path)
  hailstones = File.open(file_path).read().split("\n").map { |h| ps, vs = h.split(" @ "); p = ps.split(", "); v = vs.split(", "); p = {"x" => p[0], "y" => p[1]}; v = {"x" => v[0], "y" => v[1]}; {"p" => p, "v" => v}}

  intersections = 0
  for i in 0..hailstones.length-1 do
    for j in i..hailstones.length-1 do
      next if i == j
      hailstone1 = hailstones[i]
      hailstone2 = hailstones[j]

      eq1 = {"a" => BigDecimal(hailstone1["v"]["x"]), "b" => -BigDecimal(hailstone2["v"]["x"]), "c" => BigDecimal(hailstone2["p"]["x"]) - BigDecimal(hailstone1["p"]["x"])}
      eq2 = {"a" => BigDecimal(hailstone1["v"]["y"]), "b" => -BigDecimal(hailstone2["v"]["y"]), "c" => BigDecimal(hailstone2["p"]["y"]) - BigDecimal(hailstone1["p"]["y"])}

      t1, t2 = solve_linear_equations(eq1, eq2)

      next if t1 == nil or t2 == nil # Stones don't cross paths

      next if t1 <= BigDecimal("0") or t2 <= BigDecimal("0") # Stones cross paths in the past

      x = BigDecimal(hailstone1["v"]["x"]) * t1 + BigDecimal(hailstone1["p"]["x"])
      y = BigDecimal(hailstone1["v"]["y"]) * t1 + BigDecimal(hailstone1["p"]["y"])

      next if not (LIMITS[file_path]["MIN"] <= x and x <= LIMITS[file_path]["MAX"] and LIMITS[file_path]["MIN"] <= y and y <= LIMITS[file_path]["MAX"]) # Stones cross paths outside test area

      intersections = intersections + 1
    end
  end
  print("[#{file_path}]: #{intersections}\n")
end

solve('sample.txt')
solve('input.txt')
