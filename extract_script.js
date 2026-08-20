const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const scripts = [];
let regex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
let match;
while ((match = regex.exec(content)) !== null) {
    if (match[1].trim()) {
        fs.writeFileSync('temp_script.js', match[1]);
        break; // just the first one
    }
}
