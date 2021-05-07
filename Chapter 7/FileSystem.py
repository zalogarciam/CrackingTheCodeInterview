from datetime import datetime


from collections import Counter
class FileSystem:
    def __init__(self):
        self.entries = Counter()

    def create(self, entry):
        if isinstance(entry, Directory):
            full_path = entry.path + entry.name
            if full_path not in self.entries:
                self.entries[full_path] = []
            else:
                self.entries.get[full_path].append(entry.name)
                entry.content.append(entry.name)

        if isinstance(entry, File):
            if entry.path in self.entries:
                self.entries[entry.path].append(entry.name)
            else:
                print('Error, path', entry.path,'does not exist')

    def print_entry_info(self, entry):
        print()
        print('Name', entry.name)
        print('Path', entry.path)
        print('Created', entry.creation_date)
        print('Last Update', entry.last_update_date)
        print('Last Access', entry.last_access_date)
        print()

    def print_all(self):
        print(self.entries)


class Entry:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.creation_date = datetime.now()
        self.last_update_date = datetime.now()
        self.last_access_date = datetime.now()


class Directory(Entry):
    def __init__(self, name, path):
        Entry.__init__(self, name, path)
        self.content = []


class File(Entry):
    pass


file_system = FileSystem()
directory = Directory('files', 'D:/')
directory2 = Directory('imgs', 'D:/')
file = File('text.doc', 'D:/files')
file2 = File('presentation.ppt', 'D:/files')
file3 = File('book.doc', 'D:/files')
file4 = File('him.png', 'D:/imgs')
file4 = File('me.png', 'D:/test')

file_system.create(directory)
file_system.create(directory2)
file_system.create(file)
file_system.create(file2)
file_system.create(file3)
file_system.create(file4)

file_system.print_all()
file_system.print_entry_info(file)
file_system.print_entry_info(directory2)