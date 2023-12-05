<?php

$almanac = file_get_contents("input.txt");

$almanac_parts = explode("\n\n", $almanac);

$seeds = explode(" ", explode(": ", $almanac_parts[0])[1]);

$seed_to_soil_map = substr($almanac_parts[1], strpos($almanac_parts[1], "\n") + 1);
$soil_to_fertilizer_map = substr($almanac_parts[2], strpos($almanac_parts[2], "\n") + 1);
$fertilizer_to_water_map = substr($almanac_parts[3], strpos($almanac_parts[3], "\n") + 1);
$water_to_light_map = substr($almanac_parts[4], strpos($almanac_parts[4], "\n") + 1);
$light_to_temperature_map = substr($almanac_parts[5], strpos($almanac_parts[5], "\n") + 1);
$temperature_to_humidity_map = substr($almanac_parts[6], strpos($almanac_parts[6], "\n") + 1);
$humidity_to_location_map = substr($almanac_parts[7], strpos($almanac_parts[7], "\n") + 1);

function get_destination(string $source, string $map) {
  $lines = explode("\n", $map);
  $destination = $source;
  foreach ($lines as $line) {
    [$destination_range_start, $source_range_start, $range_length] =  explode(" ", $line);

    if ($source < $source_range_start or $source > $source_range_start + $range_length) continue;

    $destination = $destination_range_start + ($source - $source_range_start);

    break;
  }
  return $destination;
}

$all_locations = [];
foreach ($seeds as $seed) {
  $soil = get_destination($seed, $seed_to_soil_map);
  $fertilizer = get_destination($soil, $soil_to_fertilizer_map);
  $water = get_destination($fertilizer, $fertilizer_to_water_map);
  $light = get_destination($water, $water_to_light_map);
  $temperature = get_destination($light, $light_to_temperature_map);
  $humidity = get_destination($temperature, $temperature_to_humidity_map);
  $location = get_destination($humidity, $humidity_to_location_map);
  array_push($all_locations, $location);
}

$lowest_location = min($all_locations);

print_r("[input.txt]: $lowest_location\n");
