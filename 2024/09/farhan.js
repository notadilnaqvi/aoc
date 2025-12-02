const fs = require("fs");

const createIDString = (line) => {
  let formatedArray = [];
  let fileNumber = 0;

  line.forEach((num, index) => {
    const number = Number(num);
    if (index % 2 === 0) {
      formatedArray = formatedArray.concat(
        Array(number).fill(fileNumber.toString()),
      );

      fileNumber = fileNumber + 1;
    } else {
      formatedArray = formatedArray.concat(Array(number).fill("."));
    }
  });
  return formatedArray;
};

function shiftNumbersToLeft(inputArray) {
  for (let i = 0; i < inputArray.length; i++) {
    if (inputArray[i] === ".") {
      for (let j = inputArray.length - 1; j > i; j--) {
        if (inputArray[j] !== ".") {
          inputArray[i] = inputArray[j];
          inputArray[j] = ".";
          break;
        }
      }
    }
  }
  return inputArray;
}

const getSum = (updatedArray) => {
  let result = 0;
  for (let i = 0; i < updatedArray.length; i++) {
    if (updatedArray[i] !== ".") {
      result = result + Number(updatedArray[i]) * i;
    }
  }
  return result;
};

const input = fs.readFileSync("input.txt", "utf8");
const line = input.split("");

const formatedArray = createIDString(line);
const updatedArray = shiftNumbersToLeft(formatedArray);
const result = getSum(updatedArray);

console.log("result", result);
