<?php

$engine_schematic = file_get_contents("input.txt");

$special_chars = array('&', '/', '$', '#', '*', '-', '%', '=', '+', '@');

$lines = explode("\n", $engine_schematic);

$row_count = count($lines);
$col_count = strlen($lines[0]);

preg_match_all('/\d+/', str_replace("\n", "", str_replace("\n", "", $engine_schematic)), $matches, PREG_OFFSET_CAPTURE);

$part_members = array();
foreach ($matches[0] as $match) {
  $matched_number = $match[0];
  $matched_index = $match[1];

  $neighbours = get_neighbours($matched_index, strlen((string)$matched_number));

  foreach ($neighbours as $neighbour) {
    if (in_array($neighbour, $special_chars)) {
      array_push($part_members, $matched_number);
      break;
    }
  }
}

$sum_of_part_numbers = array_sum($part_members);

print_r("[input.txt] $sum_of_part_numbers\n");


function get_neighbours($index, $number_of_digits) {
  global $col_count;
  global $row_count;
  global $lines;

  $neighbours_xys = array();
  [$x, $y] = get_xy_from_index($index);

  // Quick scan of the input shows there are only 2 and 3 digit numbers
  // so we only handle 2 cases but this can be generalized to handle any
  // number of digits

  if ($number_of_digits === 1) {
    //   -1 0 1
    // -1 * * *
    //  0 * d *
    //  1 * * *

    array_push($neighbours_xys, [$x - 1, $y - 1]);
    array_push($neighbours_xys, [$x - 1, $y + 0]);
    array_push($neighbours_xys, [$x - 1, $y + 1]);

    array_push($neighbours_xys, [$x + 0, $y - 1]);
    array_push($neighbours_xys, [$x + 0, $y + 1]);

    array_push($neighbours_xys, [$x + 1, $y - 1]);
    array_push($neighbours_xys, [$x + 1, $y + 0]);
    array_push($neighbours_xys, [$x + 1, $y + 1]);
  } else if ($number_of_digits === 2) {
    //   -1 0 1 2
    // -1 * * * *
    //  0 * d d *
    //  1 * * * *

    array_push($neighbours_xys, [$x - 1, $y - 1]);
    array_push($neighbours_xys, [$x - 1, $y + 0]);
    array_push($neighbours_xys, [$x - 1, $y + 1]);

    array_push($neighbours_xys, [$x + 0, $y - 1]);
    array_push($neighbours_xys, [$x + 0, $y + 1]);

    array_push($neighbours_xys, [$x + 1, $y - 1]);
    array_push($neighbours_xys, [$x + 1, $y + 1]);

    array_push($neighbours_xys, [$x + 2, $y - 1]);
    array_push($neighbours_xys, [$x + 2, $y + 0]);
    array_push($neighbours_xys, [$x + 2, $y + 1]);
  } else if ($number_of_digits === 3) {
    //   -1 0 1 2 3
    // -1 * * * * *
    //  0 * d d d *
    //  1 * * * * *

    array_push($neighbours_xys, [$x - 1, $y - 1]);
    array_push($neighbours_xys, [$x - 1, $y + 0]);
    array_push($neighbours_xys, [$x - 1, $y + 1]);

    array_push($neighbours_xys, [$x + 0, $y - 1]);
    array_push($neighbours_xys, [$x + 0, $y + 1]);

    array_push($neighbours_xys, [$x + 1, $y - 1]);
    array_push($neighbours_xys, [$x + 1, $y + 1]);

    array_push($neighbours_xys, [$x + 2, $y - 1]);
    array_push($neighbours_xys, [$x + 2, $y + 1]);

    array_push($neighbours_xys, [$x + 3, $y - 1]);
    array_push($neighbours_xys, [$x + 3, $y + 0]);
    array_push($neighbours_xys, [$x + 3, $y + 1]);
  } else {
    throw new Exception("Not implemented yet");
  }

  $neighbours = array();
  foreach ($neighbours_xys as $neighbour_xy) {
    [$neighbour_x, $neighbour_y] = $neighbour_xy;
    if (($neighbour_x >= 0) and ($neighbour_y >= 0)  and ($neighbour_x < $col_count) and ($neighbour_y < $row_count)) {
      $neighbours_value = mb_substr($lines[$neighbour_y], $neighbour_x, 1);
      array_push($neighbours, $neighbours_value);
    }
  }
  return $neighbours;
}

function get_xy_from_index($index) {
  global $col_count;
  $x = $index % $col_count;
  $y = floor($index / $col_count);
  return array($x, $y);
}
