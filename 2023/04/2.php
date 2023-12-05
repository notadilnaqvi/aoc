<?php

$pile_of_cards = file_get_contents("input.txt");

$all_cards = explode("\n", $pile_of_cards);

function format_single_digit_numbers($string) {
  return preg_replace("/(\s)(\d)$/", '0${2}', preg_replace("/(\s)(\d)(\s)/", '0${2} ', $string));
}

$winning_numbers_in_each_card = [];
foreach ($all_cards as $card) {
  $numbers_you_have = explode(" ", format_single_digit_numbers(explode(" | ", $card)[1]));
  $winning_numbers = explode(" ", format_single_digit_numbers(explode(": ", explode(" | ", $card)[0])[1]));
  $card_name = explode(": ", explode(" | ", $card)[0])[0];

  $matches = array_intersect($numbers_you_have, $winning_numbers);

  $winning_numbers_in_each_card[] = count($matches);
}

function get_number_of_won_cards($card_index) {
  global $winning_numbers_in_each_card;

  if ($winning_numbers_in_each_card[$card_index] === 0) {
    return 0;
  } else {
    $number_of_won_cards = $winning_numbers_in_each_card[$card_index];
    for ($i = $card_index + 1; $i < $card_index + $winning_numbers_in_each_card[$card_index] + 1; $i++) {
      $number_of_won_cards += get_number_of_won_cards($i);
    }
    return $number_of_won_cards;
  }
}

$total_winnings = count($winning_numbers_in_each_card);
for ($i = 0; $i < count($winning_numbers_in_each_card); $i++) {
  $total_winnings += get_number_of_won_cards($i);
}

print_r("[input.txt]: $total_winnings\n");