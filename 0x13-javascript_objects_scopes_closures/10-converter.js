#!/usr/bin/node

exports.converter = function (base) {
  if (base > 1) {
    return function convertToBase (num) {
      if (num < base) {
        return num.toString(base);
      } else {
        const quotient = Math.floor(num / base);
        const remainder = num % base;
        return convertToBase(quotient) + remainder.toString(base);
      }
    };
  }
};
