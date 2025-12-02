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

const numOfFreeSpaces = disk.match(/\./g).length;

let compactedDisk = compactDisk(disk);

console.log(compactedDisk);

function compactDisk(disk) {
  const firstFreeSpace = [...disk].findIndex((e) => e === ".");

  const allFreeSpace = disk.substring(firstFreeSpace + 1);

  console.log(".".repeat(numOfFreeSpaces));


  const isCompacted = allFreeSpace === ".".repeat(numOfFreeSpaces)

  if (isCompacted) {
    return disk;
  }

  const last = [...disk].findLast((e) => e !== ".");
  const lastIndex = [...disk].lastIndexOf(last);
  disk = disk.replace(".", last);
  const diskArr = [...disk];
  diskArr[lastIndex] = ".";
  disk = diskArr.join("");
  return compactDisk(disk);
}
