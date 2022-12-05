# File Location

The `locate` command is used to find eligible documents, it will go to the database where the names of documents and directories are stored, to find the documents or directories that meet the conditions of the model style.

Once new file has been created we need to execute the `sudo updatedb` command to save the new file to the database.

![lab-file-location-1-1](assets/lab-file-location-2-1.png)

![lab-file-location-1-2](assets/lab-file-location-2-2.png)

## Locate File With Full Name

The `locate test.cpp` command will search the system for all files named test.cpp, the result is retrieved from the database.

```bash
locate test.cpp
```

![lab-file-location-2-3](assets/lab-file-location-2-3.png)

## Locate Files With Regular Formula

The `locate *.cpp` command will search the system for all files whose name contains *.cpp, the result is retrieved from the database.

```bash
locate *.cpp
```

![lab-file-location-2-4](assets/lab-file-location-2-4.png)

![lab-file-location-2-5](assets/lab-file-location-2-5.png)

## Locate Files in the Specified Directory

The `locate ~/lab/*.cpp` command will search all files in the specified directory, the result is retrieved from the database.

```bash
locate ~/lab/*.cpp
```

![lab-file-location-3-1](assets/lab-file-location-2-6.png)

