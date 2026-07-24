import os
import fnmatch


def count_lines_in_file(filepath):
    """Подсчитывает количество строк в файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return sum(1 for line in f)
    except (UnicodeDecodeError, PermissionError, OSError):
        # Пропускаем бинарные файлы и файлы без доступа
        return 0


def is_code_file(filename):
    """Проверяет, является ли файл файлом с кодом"""
    code_extensions = {
        '.py', '.js', '.java', '.c', '.cpp', '.h', '.hpp', '.cs',
        '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.ts',
        '.html', '.css', '.scss', '.less', '.xml', '.yaml',
        '.yml', '.sql', '.sh', '.bash', '.bat', '.ps1', '.md',
    }
    return any(filename.endswith(ext) for ext in code_extensions)


def should_ignore_directory(dirname):
    """Проверяет, нужно ли игнорировать директорию"""
    ignore_dirs = {
        '.git', '__pycache__', 'node_modules', 'venv', 'env',
        '.venv', 'dist', 'build', 'target', 'bin', 'obj',
        'vendor', 'coverage', '.idea', '.vscode', '.vs',
        'Files'
    }
    return dirname in ignore_dirs


def count_code_lines(directory='.'):
    """Рекурсивно подсчитывает строки кода во всех файлах"""
    total_lines = 0
    file_count = 0
    results = {}

    for root, dirs, files in os.walk(directory):
        # Игнорируем системные директории
        dirs[:] = [d for d in dirs if not should_ignore_directory(d)]

        for file in files:
            if is_code_file(file):
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, directory)
                lines = count_lines_in_file(filepath)

                if lines > 0:
                    total_lines += lines
                    file_count += 1
                    results[relative_path] = lines

    return total_lines, file_count, results


def print_results(total_lines, file_count, results):
    """Выводит результаты подсчета"""
    print("=" * 60)
    print(f"ОБЩАЯ СТАТИСТИКА:")
    print(f"Всего файлов с кодом: {file_count}")
    print(f"Всего строк кода: {total_lines}")
    print("=" * 60)

    # Сортируем файлы по количеству строк (по убыванию)
    sorted_files = sorted(results.items(), key=lambda x: x[1], reverse=True)

    print("\nДЕТАЛЬНАЯ СТАТИСТИКА (топ 20 файлов):")
    for i, (filepath, lines) in enumerate(sorted_files[:20], 1):
        print(f"{i:2d}. {filepath}: {lines} строк")

    if len(sorted_files) > 20:
        print(f"... и еще {len(sorted_files) - 20} файлов")


def main():
    """Основная функция"""
    current_dir = os.getcwd()
    print(f"Подсчет строк кода в директории: {current_dir}")
    print("Поиск файлов...")

    total_lines, file_count, results = count_code_lines(current_dir)

    if file_count == 0:
        print("Не найдено файлов с кодом!")
        return

    print_results(total_lines, file_count, results)


if __name__ == "__main__":
    main()

    #