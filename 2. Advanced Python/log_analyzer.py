# Class for Analyzing Logs
class LogAnalyzer:

    # Method to Initialize the class
    def __init__(self, filename):
        self.filename = filename
    
    # Method to Load the logs
    def load_logs(self):
        """
        Use a generator to load the log file line by line
        """
        with open (self.filename, "r") as f:

            # Iterate through the log file and yield each line
            for line in f:
                yield line.strip()

    # Method to Count the Levels
    def count_levels(self):
        """
        Count the number of log levels
        """
        levels = {}

        # Iterate through the log file and count the number of log levels
        for line in self.load_logs():
            key = line.split()[2]

            # Check if the level is already in the dictionary
            if key not in levels:
                levels[key] = 1
            else:
                levels[key] += 1
        return levels

    # Method to get all the error logs
    def get_errors(self):
        """
        Get all the error logs
        """
        errors = []
        
        # Check if the level is "ERROR"
        for line in self.load_logs():
            level = line.split()[2]
            if level == "ERROR":
                errors.append(line)
        return errors
    
    # Method to search for a keyword
    def search(self, keyword):
        """
        Search for a keyword in the log file
        """
        results = []

        # Check if the keyword is in the line
        for line in self.load_logs():
            if keyword.lower() in line.lower():
                results.append(line)
        return results

# Main Function
analyzer = LogAnalyzer("2. Advanced Python/app.log")

print(analyzer.count_levels())
print(analyzer.get_errors())
print(analyzer.search("Database"))

