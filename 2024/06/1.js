const fs = require("node:fs");

const input = fs.readFileSync("input.txt", "utf8");

const map = input.split("\n").map((r) => r.split(''));

const rowCount = map.length;
const colCount = map.at(0).length;

const movements = {
  "^": [0, -1],
  "v": [0, 1],
  "<": [-1, 0],
  ">": [1, 0],
};

const toRight = {
  "^": ">",
  "v": "<",
  "<": "^",
  ">": "v",
};

let guardPos = xyFromIndex(
  input
    .replaceAll("\n", "")
    .split("")
    .findIndex((tile) => "^v><".includes(tile)),
);

let guardDir = input
  .replaceAll("\n", "")
  .split("")
  .find((tile) => !".#".includes(tile));

const travelled = [guardPos];

while (
  0 <= guardPos[0] &&
  guardPos[0] < colCount &&
  0 <= guardPos[1] &&
  guardPos[1] < rowCount
) {
  const { newPos, newDir, out } = move(guardPos, guardDir);
  if (out) break;
  travelled.push(newPos);
  guardPos = newPos;
  guardDir = newDir;
}

console.log(Array.from(new Set(travelled.map(JSON.stringify)), JSON.parse).length);

function xyFromIndex(index) {
  return [index % colCount, Math.floor(index / colCount)];
}

function move(currPos, currDir) {
  const nextX = currPos[0] + movements[currDir][0];
  const nextY = currPos[1] + movements[currDir][1];

  if (
    typeof map[nextY] === "undefined" ||
    typeof !map[nextY][nextX] === "undefined"
  ) {
    return { out: 1 };
  }
  const next = map[nextY][nextX];

  if (next === "." || "^v><".includes(next)) {
    return {
      newPos: [nextX, nextY],
      newDir: currDir,
    };
  } else if (next === "#") {
    return {
      newPos: [
        currPos[0] + movements[toRight[currDir]][0],
        currPos[1] + movements[toRight[currDir]][1],
      ],
      newDir: toRight[currDir],
    };
  } else {
    throw new Error("fuck me: " + next);
  }
}
