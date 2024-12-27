const fs = require("node:fs");

const input = fs.readFileSync("input.txt", "utf8");

const allRules = input.split("\n\n")[0].split("\n");
const updates = input.split("\n\n")[1].split("\n");

const map = {};
const nums = [];

for (const rule of allRules) {
  const [fn, sn] = rule.split("|").map(Number);
  if (!nums.includes(fn)) nums.push(fn);
  if (!nums.includes(sn)) nums.push(sn);
}

for (const num of nums) {
  const numRules = allRules.filter((r) => r.includes(num.toString()));
  map[num] = { before: [], after: [] };
  for (const numRule of numRules) {
    const [fn, sn] = numRule.split("|").map(Number);
    if (fn === num && !map[num].after.includes(sn)) {
      map[num].after.push(sn);
    } else if (sn === num && !map[num].before.includes(fn)) {
      map[num].before.push(fn);
    } else {
      throw new Error("fuck");
    }
  }
}

let ans = 0;
for (const update of updates) {
  const pages = update.split(",").map(Number);
  let isInOrder = true;
  for (let i = 0; i < pages.length - 1; i++) {
    for (let j = i + 1; j < pages.length; j++) {
      if (!comesAfter(pages[i], pages[j])) {
        isInOrder = false;
        break;
      }
    }
  }
  if (isInOrder) {
    ans += pages[Math.floor((0 + pages.length - 1) / 2)];
  }
}

console.log(ans)

// Checks if num2 comes after num1
function comesAfter(num1, num2) {
  const num1order = map[num1];
  const num2order = map[num2];
  return num1order.after.includes(num2) && num2order.before.includes(num1);
}
