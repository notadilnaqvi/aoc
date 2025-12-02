const fs = require("node:fs");

const diskMap = fs.readFileSync("sample.txt", "utf8");

function diskMapToDisk(diskMap) {
  let id = 0;
  let disk = "";
  for (let i = 0; i < diskMap.length; i++) {
    if (i % 2 == 0) {
      const blocksCount = Number(diskMap[i]);
      for (let b = 0; b < blocksCount; b++) {
        disk += String(id);
      }
      id++;
    } else {
      const freeSpace = Number(diskMap[i]);
      for (let f = 0; f < freeSpace; f++) {
        disk += ".";
      }
    }
  }

  return disk;
}

const disk = diskMapToDisk(diskMap);

let compactedDisk = disk;
let loops = 0;
while (true && loops < 1000) {
  loops++;
  compactedDisk = compactDisk(compactedDisk);
  const firstFreeSpace = compactedDisk.indexOf(".");

  const allBlocks = [...compactedDisk.substring(0, firstFreeSpace)];
  const allFreeSpace = [...compactedDisk.substring(firstFreeSpace + 1)];
  const isCompacted =
    allBlocks.every((e) => e !== ".") && allFreeSpace.every((e) => e === ".");

  if (isCompacted) {
    break;
  }
}

console.log(compactedDisk)

function compactDisk(disk) {
  const last = [...disk].findLast((e) => e !== ".");
  const lastIndex = disk.lastIndexOf(last);
  disk = disk.replace(".", last);
  const diskArr = [...disk];
  diskArr[lastIndex] = ".";
  disk = diskArr.join("");
  return disk;
}
