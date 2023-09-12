#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const NewList = [];
  let i;

  if (len > 1) {
    for (i = 0; i < len; i++) {
      NewList[i] = list[len - i - 1];
    }
    return NewList;
  } else {
    return list;
  }
};
