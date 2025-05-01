let start = "**"; // starting from 2
let end = "**********"; // 10 stars (length = 10)

for (let i = start; i.length <= end.length; i += "*") {
  console.log(i.length);
}
