const fs = require("node:fs");

const file = fs.readFileSync("input.txt", "utf8");

const mulRe = /mul\(\d{1,3},\d{1,3}\)/g;

const insRe = /(?<=don't\(\))(.*?)(?=do\(\))/;

const insMatches = file.match(insRe);

console.log(file);
console.log(insMatches);

let fileCopy = file;
for (const insMatch of insMatches) {
  fileCopy = fileCopy.replace(insMatch, "");
}

const mulMatches = fileCopy.match(mulRe);

let ans = 0
for (const mulMatch of mulMatches) {
  ans += mul(mulMatch)
}

console.log("ans", ans);

function mul(str) {
  const [a, b] = str.replace("mul(", "").replace(")", "").split(",");
  return a * b;
}
