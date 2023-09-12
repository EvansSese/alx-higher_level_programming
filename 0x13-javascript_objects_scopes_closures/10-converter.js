#!/usr/bin/node

exports.converter = function (base) {
  if (base > 1) {
    return function convertToBase (num) {
      if (num < base) return num.toString(base);
      return (convertToBase(Math.floor(num / base)) + (num % base).toString(base));
    };
  }
};
