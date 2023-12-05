<?php

$pile_of_cards = file_get_contents("input.txt");

$all_cards = explode("\n", $pile_of_cards);

function format_single_digit_numbers($string) {
  return preg_replace("/(\s)(\d)$/", '0${2}', preg_replace("/(\s)(\d)(\s)/", '0${2} ', $string));
}

function calculate_card_worth($number_of_matches) {
  if ($number_of_matches === 0) return 0;
  return pow(2, $number_of_matches - 1);
}

$worth_of_all_cards = 0;
foreach ($all_cards as $card) {
  $numbers_you_have = explode(" ", format_single_digit_numbers(explode(" | ", $card)[1]));
  $winning_numbers = explode(" ", format_single_digit_numbers(explode(": ", explode(" | ", $card)[0])[1]));
  $card_name = explode(": ", explode(" | ", $card)[0])[0];

  $matches = array_intersect($numbers_you_have, $winning_numbers);

  $worth_of_all_cards += calculate_card_worth(count($matches));

}
print_r("[input.txt]: $worth_of_all_cards\n"); 

