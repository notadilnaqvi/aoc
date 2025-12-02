const fs = require("node:fs");

const input = fs.readFileSync("sample.txt", "utf8");

const equations = input.split("\n");

const operands = ["+", "*"];
for (const equation of equations) {
  const expectedResult = Number(equation.split(":")[0]);
  const numbers = equation.split(":")[1].trim().split(" ").map(Number);

  let sums = numbers[0];
  let products = numbers[0];
  numbers.forEach((_, index) => {
    if (!numbers[index + 1]) return;
    const sum = result + numbers[index + 1];
    const product = result * numbers[index + 1];
  })
  console.log("====");
}

function calc( numbers, target) {
  if (numbers.length === 1) return numbers[0];
}