const fs = require("node:fs");

function calculateDeterminant(p1, p2) {
  return p1.x * p2.y - p2.x * p1.y;
}

const directionMap = {
  0: "R",
  1: "D",
  2: "L",
  3: "U",
};

function solve(filePath) {
  const digPlan = fs.readFileSync(filePath, "utf8");

  const instructionsStr = digPlan.split("\n");

  const instructions = [];
  for (const instructionStr of instructionsStr) {
    let hex = instructionStr
      .split(" ")[2]
      .replace("(", "")
      .replace(")", "")
      .replace("#", "");
      
    const direction = directionMap[hex.at(-1)];
    const meters = parseInt(hex.slice(0, -1), 16);
    
    instructions.push({
      direction: direction,
      meters: meters,
    });
  }

  let perimater = 0;
  const startingPoint = { x: 0, y: 0 };
  let previousPoint = startingPoint;
  const polygon = [];
  for (const instruction of instructions) {
    const newPoint = { ...previousPoint };
    perimater = perimater + instruction.meters;
    switch (instruction.direction) {
      case "R": {
        newPoint.x = newPoint.x + instruction.meters;
        break;
      }
      case "D": {
        newPoint.y = newPoint.y + instruction.meters;
        break;
      }
      case "L": {
        newPoint.x = newPoint.x - instruction.meters;
        break;
      }
      case "U": {
        newPoint.y = newPoint.y - instruction.meters;
        break;
      }
      default: {
        throw Error("dumb");
      }
    }
    polygon.push({ ...newPoint });
    previousPoint = newPoint;
  }

  let sumOfDeterminemts = 0;
  for (let i = 0; i < polygon.length; i++) {
    const p1 = polygon[i];
    const p2 = polygon[i + 1 >= polygon.length ? 0 : i + 1];
    sumOfDeterminemts = sumOfDeterminemts + calculateDeterminant(p1, p2);
  }

  const integerPointsOnBoundary = perimater;
  const area = sumOfDeterminemts / 2; // https://en.wikipedia.org/wiki/Shoelace_formula
  const integerPointsInsidePolygon = area + 1 - integerPointsOnBoundary / 2; // https://en.wikipedia.org/wiki/Pick's_theorem
  const lavaCapacity = integerPointsInsidePolygon + integerPointsOnBoundary;

  console.log("[" + filePath + "]: " + lavaCapacity);
}

solve("sample.txt");
solve("input.txt");
