#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  let new_list = [];
  let i;

  if (len > 1) {
    for (i = 0; i < len; i++) {
      new_list[i] = list[len - i - 1];
    }
    return new_list;
  } else {
    return list;
  }
}