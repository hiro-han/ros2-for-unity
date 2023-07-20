import os
import sys

print(sys.argv)
if len(sys.argv) < 2:
    sys.exit()

base_dir = sys.argv[1]

for root, dirs, files in os.walk(top=base_dir):
    for file in files:
        ext = os.path.splitext(file)[-1]
        filePath = os.path.join(root, file)
        if (ext == ".meta"):
            with open(filePath) as reader:
                content = reader.readlines()
            
            is_header_end = False
            is_footer_start = False
            header = ""
            footer = ""

            android_platform_setting = (\
                "  - first:\n"
                "      : Any\n"
                "    second:\n"
                "      enabled: 0\n"
                "      settings:\n"
                "        Exclude Android: 0\n"
                "        Exclude Editor: 1\n"
                "        Exclude Linux64: 1\n"
                "        Exclude OSXUniversal: 1\n"
                "        Exclude WebGL: 1\n"
                "        Exclude Win: 1\n"
                "        Exclude Win64: 1\n"
                "  - first:\n"
                "      Android: Android\n"
                "    second:\n"
                "      enabled: 1\n"
                "      settings:\n"
                "        CPU: ARM64\n"
                "  - first:\n"
                "      Any: \n"
                "    second:\n"
                "      enabled: 0\n"
                "      settings: {}\n")
            
            for line in content:
                # print(line, end="")
                if "userData:" in line:
                    is_footer_start = True
                    
                if is_header_end is False:
                    header += line
                elif is_footer_start is True:
                    footer += line
                    
                if "platformData:" in line:
                    is_header_end = True

            meta_item = header + android_platform_setting + footer
            # print(is_header_end)
            # print(is_footer_start)
            # print("----- Header -----")
            # print(header)
            # print("----- Setting -----")
            # print(android_platform_setting)
            # print("----- Footer -----")
            # print(footer)
            # print("----- Meta -----")
            # print(meta_item)

            with open(filePath, 'w') as writer:
                writer.write(meta_item)