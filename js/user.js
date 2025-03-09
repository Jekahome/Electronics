function convertCapacity() {
  const value = parseFloat(document.getElementById("valueConvertCapacity").value);
  const fromUnit = document.getElementById("fromUnitConvertCapacity").value;
  const toUnit = document.getElementById("toUnitConvertCapacity").value;
  let result;

  if (isNaN(value)) {
      document.getElementById("resultConvertCapacity").textContent = "Ввод отсутствует.";
      return;
  }
  if (value < 0) {
      document.getElementById("resultConvertCapacity").textContent = "Введите положительное число.";
      return;
  }

  const units = {
      F: 1,
      cF: 1e-2,
      mF: 1e-3,
      uF: 1e-6,
      nF: 1e-9,
      pF: 1e-12,
      fF: 1e-15,
  };

  const valueInFarads = value * units[fromUnit];
  result = valueInFarads / units[toUnit];

  // Функция для форматирования числа в полной форме
  const formatNumber = (num) => {
      if (Math.abs(num) < 1e-6) {
          // Для очень маленьких чисел используем toFixed
          return num.toFixed(20).replace(/\.?0+$/, ''); // Убираем лишние нули после запятой
      } else {
          // Для больших чисел используем toLocaleString
          return num.toLocaleString('fullwide', { useGrouping: false, maximumFractionDigits: 20 });
      }
  };

  // Функция для добавления экспоненциальной записи в скобках
  const addExponentialNotation = (num) => {
      return ` (${num.toExponential()})`;
  };

  const formattedResult = formatNumber(result);
  const formattedFarads = formatNumber(valueInFarads);

  let faradsResult = "";
  if (toUnit !== "F") {
      faradsResult = ` = ${formattedFarads} F${addExponentialNotation(valueInFarads)}`;
  }

  document.getElementById("resultConvertCapacity").textContent = 
      `${value} ${fromUnit} = ${formattedResult} ${toUnit}${addExponentialNotation(result)}${faradsResult}`;
}

function convertInductance(){
    const value = parseFloat(document.getElementById("valueConvertInductance").value);
    const fromUnit = document.getElementById("fromUnitConvertInductance").value;
    const toUnit = document.getElementById("toUnitConvertInductance").value;
    let result;
  
    if (isNaN(value)) {
        document.getElementById("resultConvertInductance").textContent = "Ввод отсутствует.";
        return;
    }
    if (value < 0) {
        document.getElementById("resultConvertInductance").textContent = "Введите положительное число.";
        return;
    }
  
    const units = {
        H: 1,
        cH: 1e-2,
        mH: 1e-3,
        uH: 1e-6,
        nH: 1e-9,
        pH: 1e-12,
        fH: 1e-15,
    };
  
    const valueInFarads = value * units[fromUnit];
    result = valueInFarads / units[toUnit];
  
    // Функция для форматирования числа в полной форме
    const formatNumber = (num) => {
        if (Math.abs(num) < 1e-6) {
            // Для очень маленьких чисел используем toFixed
            return num.toFixed(20).replace(/\.?0+$/, ''); // Убираем лишние нули после запятой
        } else {
            // Для больших чисел используем toLocaleString
            return num.toLocaleString('fullwide', { useGrouping: false, maximumFractionDigits: 20 });
        }
    };
  
    // Функция для добавления экспоненциальной записи в скобках
    const addExponentialNotation = (num) => {
        return ` (${num.toExponential()})`;
    };
  
    const formattedResult = formatNumber(result);
    const formattedFarads = formatNumber(valueInFarads);
  
    let faradsResult = "";
    if (toUnit !== "H") {
        faradsResult = ` = ${formattedFarads} H${addExponentialNotation(valueInFarads)}`;
    }
  
    document.getElementById("resultConvertInductance").textContent = 
        `${value} ${fromUnit} = ${formattedResult} ${toUnit}${addExponentialNotation(result)}${faradsResult}`;    
}