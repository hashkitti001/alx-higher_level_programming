#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction.call();
    i += 1;
  }
};
