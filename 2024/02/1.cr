lines = File.read_lines("input.txt")

ans = 0

lines.each_with_index do |report, i|
  safe = false
  diffs = [] of Int32
  levels = report.split
  levels.each_with_index do |_, j|
    if j + 1 >= levels.size
      break
    end
    diff = levels[j].to_i - levels[j + 1].to_i
    diffs << diff
  end

  # The levels are either all increasing or all decreasing.
  pos_diffs = diffs.clone.select! { |x| x > 0 }
  neg_diffs = diffs.clone.select! { |x| x < 0 }
  is_inc = pos_diffs.size == diffs.size && neg_diffs.size == 0
  is_dec = neg_diffs.size == diffs.size && pos_diffs.size == 0

  # Any two adjacent levels differ by at least one and at most three.
  diff_too_large = false
  diffs.each do |diff|
    if !(diff.abs == 1 || diff.abs == 2 || diff.abs == 3)
      diff_too_large = true
      break
    end
  end

  if (is_inc || is_dec) && !diff_too_large
    ans += 1
  end
end

puts ans