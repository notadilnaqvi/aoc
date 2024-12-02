lines = File.read_lines("input.txt")

ans = 0

def is_report_safe(levels)
  diffs = [] of Int32

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

  is_safe = (is_inc || is_dec) && !diff_too_large
  return is_safe
end

lines.each_with_index do |report, i|
  levels = report.split
  if is_report_safe(levels)
    ans += 1
  else
    # Tolerate a single bad level
    Array.new(levels.size, nil).each_with_index do |_, j|
      cloned_levels = levels.clone
      cloned_levels.delete_at(j)
      if is_report_safe(cloned_levels)
        ans += 1
        break
      end
    end
  end
end

puts ans