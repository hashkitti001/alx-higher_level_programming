#!/usr/bin/node
exports.esrever = function (list) {
  const tempList = [];
  do {
    tempList.push(list.pop());
  } while (list.length > 0);
  return tempList;
};
