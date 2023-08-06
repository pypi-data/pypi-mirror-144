# Minecraft Backup

minecraft-backup is package for Minecraft Servers Backup.

To use this package, you need to run it in Therminal.

If you want it to run periodically, you will need to use software such as cron.

## How to install
```bash
$ pip install miencraft_backup
````

## How to use
```
$ minecraft-backup [-h] {backup,clear,config} ...
```

# Commands

Description of all Commands.

## Backup
This command is to backup the folder.
```
$ minecraft-backup backup [-h] [--no-log] [-z | -t | -tz] minecraft_folder backup_folder
```

### Positional
| Name | Description |
| ---- | ----------- |
| minecraft_folder | Write the Minecraft folder path. |
| backup_folder | Write the folder path should you want to save backup. |

### Options
| Normal | Short | Description |
| ------ | ----- | ------------|
| --help | -h | show help message. |
| --no-log | None | Mode to don't save the backup log. |
| -zip | -z | Mode to save and compress to zip. |
| -tar | -t | Mode to save and compress to tgz/tar.gz |
| -tar-zip | -tz | Mode to save and compress to zip and tgz/tar.gz |

## Clear
This command is to delete all logs of backup history.
```
$ minecraft-backup clear [-h]
```

### Positional
None

### Options
| Normal | Short | Description |
| ------ | ----- | ------------|
| --help | -h | show help message. |

## Config
This command is to change the config of package.
```
usage: minecraft-backup config [-h] [-lg LOGS_PATH] [-dt DELETE_TARGET] [-ad] [--no-log]
```

### Positional
None

### Options
| Normal | Short | Description | Default | Positional arguments |
| ------ | ----- | ------------| ------- | ---------- |
| --help | -h | show help message. | None | None |
| --logs-path | -lg | You can change the path of logs. | minecraft_backup.__path__/data/user_config.json | new log file path \*1 |
| --delete-target | -dt | Backup file expiration date | 7d | expiration date \*2 |
| --auto-delete | -ad | You can turn on/off auto delete | ON | NONE |
| --no-log | None | Mode to don't save the config log | None | None |

### Warning!

\*1 When you use this command you will be lost your log data. I recommend saving the files if you need to do it before doing it.

\*2 You can setting in `0y7d00h00m00s` (Or You can just setting to `7d`)
