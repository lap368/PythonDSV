// metaUtils.js

async function loadFile(tp, path) {
  let split_path = path.split("/");
  let final_seg = split_path[split_path.length - 1];

  // remove extension
  if (final_seg.includes(".")) {
    final_seg = final_seg.split(".")[0];
    split_path[split_path.length - 1] = final_seg;
  }

  const cleanPath = split_path.join("/");
  let content = "";

  try {
    content = await tp.file.include("[[" + cleanPath + "]]");
  } catch (e) {
    console.error("Error loading file at " + cleanPath + ":\n" + e);
    return { cleanPath, content: "" };
  }

  return { cleanPath, content };
}

function parseFrontmatter(content) {
  const fmMatch = content.match(/^---\n([\s\S]*?)\n---/);
  if (!fmMatch) return { fm: null, body: content };

    return { fm: fmMatch[1], body: content.substring(fmMatch[0].length) };
}

function writeFrontmatter(content, newFrontmatter) {
  if (/^---\n([\s\S]*?)\n---/.test(content)) {
    return content.replace(/^---\n([\s\S]*?)\n---/, `---\n${newFrontmatter}\n---`);
  } else {
    return `---\n${newFrontmatter}\n---\n\n${content}`;
  }
}

async function getMeta(tp, path, key, defaultValue = null) {
  const { content } = await loadFile(tp, path);
  const { fm } = parseFrontmatter(content);
  if (!fm) return defaultValue;

  const keyRegex = new RegExp(`^${key}:[ \\t]*"?([^"\\n]*)"?`, "m");
  const match = fm.match(keyRegex);
  return match ? match[1].trim() : defaultValue;
}

async function setMeta(tp, path, key, newValue) {
  const { cleanPath, content } = await loadFile(tp, path);
  const { fm } = parseFrontmatter(content);

  let newContent = content;
  if (fm) {
    const keyRegex = new RegExp(`^${key}:[ \\t]*"?([^"\\n]*)"?`, "m");
    if (keyRegex.test(fm)) {
      newContent = content.replace(keyRegex, `${key}: "${newValue}"`);
    } else {
      newContent = content.replace(
        /^---\n([\s\S]*?)\n---/,
        `---\n$1\n${key}: "${newValue}"\n---`
      );
    }
  } else {
    newContent = `---\n${key}: "${newValue}"\n---\n\n${content}`;
  }

  // Get the actual TFile
  const tfile = app.vault.getAbstractFileByPath(cleanPath + ".md");
  if (tfile) {
    await app.vault.modify(tfile, newContent);
  } else {
    console.error("setMeta: could not find file at " + cleanPath);
  }

  return newValue;
}

async function updateMeta(tp, path, key, updaterFn, defaultValue = null) {
  const oldValue = await getMeta(tp, path, key, defaultValue);
  const newValue = updaterFn(oldValue);
  await setMeta(tp, path, key, newValue);
  return { oldValue, newValue };
}

module.exports = { getMeta, setMeta, updateMeta, parseFrontmatter };
