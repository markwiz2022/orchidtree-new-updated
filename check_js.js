const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

// Extract script tags
const scripts = [];
let regex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
let match;
while ((match = regex.exec(content)) !== null) {
    if (match[1].trim()) {
        scripts.push(match[1]);
    }
}

for (let i = 0; i < scripts.length; i++) {
    try {
        new Function(scripts[i]);
        console.log(`Script ${i} is valid.`);
    } catch (e) {
        console.log(`Script ${i} has error:`, e.message);
        // Find line number
        const lines = scripts[i].split('\n');
        for (let j = 0; j < lines.length; j++) {
            try {
                new Function(lines.slice(0, j+1).join('\n'));
            } catch (err) {
                console.log(`Error likely at line ${j+1}:`, lines[j]);
                break;
            }
        }
    }
}
