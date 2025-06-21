def translate_code(code, from_lang="python", to_lang="java"):
    if from_lang == "python" and to_lang == "java":
        return "// This is a simulated translation\nSystem.out.println(\"Translated from Python\");"
    elif from_lang == "python" and to_lang == "cpp":
        return "// Simulated C++ translation\ncout << \"Hello from Python\" << endl;"
    elif from_lang == "python" and to_lang == "javascript":
        return "// Simulated JavaScript translation\nconsole.log('Hello from Python');"
    elif from_lang == "java" and to_lang == "python":
        return "# Simulated Python translation\nprint(\"Hello from Java\")"
    elif from_lang == "java" and to_lang == "cpp":
        return "// Simulated C++ translation\n#include <iostream>\nint main() { std::cout << \"Hello from Java\" << std::endl; return 0; }"
    elif from_lang == "cpp" and to_lang == "python":
        return "# Simulated Python translation\nprint(\"Hello from C++\")"
    elif from_lang == "cpp" and to_lang == "java":
        return "// Simulated Java translation\npublic class Main { public static void main(String[] args) { System.out.println(\"Hello from C++\"); } }"
    elif from_lang == "javascript" and to_lang == "python":
        return "# Simulated Python translation\nprint('Hello from JavaScript')"
    elif from_lang == "javascript" and to_lang == "java":
        return "// Simulated Java translation\npublic class Main { public static void main(String[] args) { System.out.println(\"Hello from JavaScript\"); } }"
    else:
        return "// Error: Unsupported language pair"
