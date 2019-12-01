let lineReader = require('readline').createInterface({
 	input: require('fs').createReadStream('input.txt')
});

sum = 0
lineReader.on('line', function(line) {
 	let result = Math.floor(parseInt(line) / 3) - 2
 	sum += result
 	console.log(sum)
});