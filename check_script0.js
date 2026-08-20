const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const scripts = [];
let regex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
let match;
while ((match = regex.exec(content)) !== null) {
    if (match[1].trim()) {
        scripts.push(match[1]);
    }
}
console.log(scripts[0].substring(0, 500));
