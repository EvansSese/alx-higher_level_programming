#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  let temp, i;

  if (len > 1) {
    for (i = 0; i < len; i++) {
      temp = list[i];
      list[i] = list[len - i - 1];
      list[len - i - 1] = list[i];
    }
    return list;
  } else {
    return list;
  }
}