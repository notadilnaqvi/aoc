const fs = require("node:fs");

const input = fs.readFileSync("input.txt", "utf8");

const map = input.split("\n").map((r) => r.split(""));

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

let loopsCount = 0;
for (let row = 0; row < rowCount; row++) {
  for (let col = 0; col < colCount; col++) {
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

    const newMap = structuredClone(map);

    if (map[row][col] === ".") {
      newMap[row][col] = "#";
    }

    let stepCounter = 0;
    while (true) {
      const { newPos, newDir, out } = move(guardPos, guardDir, newMap);
      stepCounter++;
      if (stepCounter > 20000) {
        loopsCount++;
        break;
      }
      if (out) {
        break;
      }
      guardPos = [...newPos];
      guardDir = newDir;
    }
  }
}

console.log("loopsCount", loopsCount);

function xyFromIndex(index) {
  return [index % colCount, Math.floor(index / colCount)];
}

function move(currPos, currDir, map) {
  const nextX = currPos[0] + movements[currDir][0];
  const nextY = currPos[1] + movements[currDir][1];

  if (
    typeof map[nextY] === "undefined" ||
    typeof map[nextY][nextX] === "undefined"
  ) {
    return { newPos: null, newDir: null, out: true };
  }
  const next = map[nextY][nextX];

  if (next === "." || "^v><".includes(next)) {
    return {
      newPos: [nextX, nextY],
      newDir: currDir,
      out: false,
    };
  } else if (next === "#") {
    return move(currPos, toRight[currDir], map)
  } else {
    throw new Error("fuck me: " + next + ", " + nextX + ", " + nextX);
  }
}

// (wrong)
// 1511 is low
