function convertCapacity() {
    const value = parseFloat(document.getElementById("valueConvertCapacity").value);
    const fromUnit = document.getElementById("fromUnitConvertCapacity").value;
    const toUnit = document.getElementById("toUnitConvertCapacity").value;
    let result;
  
    if (isNaN(value)) {
        document.getElementById("resultConvertCapacity").textContent = "Ввод отсутвет.";
        return;  
    }
    if (value < 0) {
        document.getElementById("resultConvertCapacity").textContent = "Введите положительное число.";
        return;
    }
    const units = {
      F: 1,
      mF: 1e-3,
      uF: 1e-6,
      nF: 1e-9,
      pF: 1e-12,
    };
  
    const valueInFarads = value * units[fromUnit];
  result = valueInFarads / units[toUnit];

  let faradsResult = "";
  if (toUnit !== "F") {
    faradsResult = ` = ${valueInFarads} F`;
  }

  document.getElementById("resultConvertCapacity").textContent = `${value} ${fromUnit} = ${result} ${toUnit}${faradsResult}`;
}