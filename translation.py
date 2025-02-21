class Translation(object):
    START_TEXT = """Thank You for using me.
/help to know how to use me
Source Code https://github.com/TeamMaptap/Mtuploder_bot
© @MTUploader_Bot"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "Contact @MTMOVIES_ADMIN_bot"
    #UPGRADE_TEXT = """ @MTUploader_Bot Paid Plans
#-------
#Plan: FREE
#Filesize limit: 0 MB
#Daily limit: UNLIMITED
#Price 🇮🇳: ₹ 0/Month
#FEATURES:
#👉 <a href="#">All Supported Video Formats of https://rg3.github.io/youtube-dl/supportedsites.html, except HLS videos!</a>
#👉 <a href="#">Get High Speed Direct Download Link of any Telegram file</a>
#👉 <a href="#">Get a Telegram sticker as a Telegram downloadable media</a>
#-------
#Plan: A
#Filesize limit: UNLIMITED
#Daily limit: UNLIMITED
#Price 🇮🇳: ₹ 97/Month

#FEATURES:
#👉 <a href="#">All Supported Video Formats of https://rg3.github.io/youtube-dl/supportedsites.html, except HLS videos!</a>
#👉 <a href="#">Get High Speed Direct Download Link of any Telegram file</a>
#👉 <a href="#">Get a Telegram sticker as a Telegram downloadable media</a>
#👉 <a href="#">Upload as file from any HTTP link, with custom thumbnail support</a>
#-------
#Plan: B
#Filesize limit: 1.5GB
#Daily limit: UNLIMITED
#Price 🇮🇳: ₹ 127/Month

#FEATURES:
#👉 <a href="#">All Supported Video Formats of https://rg3.github.io/youtube-dl/supportedsites.html!</a>
#👉 <a href="#">Get High Speed Direct Download Link of any Telegram file</a>
#👉 <a href="#">Get a Telegram sticker as a Telegram downloadable media</a>
#👉 <a href="#">Upload as file from any HTTP link, with custom thumbnail support</a>
#👉 <a href="#">Convert To Streamable Video, any Telegram file</a>
#👉 <a href="#">Convert To Telegram Audio, the media sent as Telegram Documents</a>
#-------
#Plan: C
#Filesize limit: 1.5GB
#Daily limit: UNLIMITED
#Price 🇮🇳: ₹ 314/Month

#FEATURES:
#👉 <a href="#">All Supported Video Formats of https://rg3.github.io/youtube-dl/supportedsites.html!</a>
#👉 <a href="#">Get High Speed Direct Download Link of any Telegram file</a>
#👉 <a href="#">Get a Telegram sticker as a Telegram downloadable media</a>
#👉 <a href="#">Upload as file from any HTTP link, with custom thumbnail support</a>
#👉 <a href="#">Convert To Streamable Video, any Telegram file</a>
#👉 <a href="#t">Convert To Telegram Audio, the media sent as Telegram Documents</a>
#👉 <a href="#">ReName Telegram files, with custom thumbnail support</a>
#-------
#Plan: D
#Filesize limit: 1.5GB
#Daily limit: UNLIMITED
#Price 🇮🇳: ₹ 987/Month

#FEATURES:
#👉 <a href="#">All Supported Video Formats of https://rg3.github.io/youtube-dl/supportedsites.html!</a>
#👉 <a href="#">Get High Speed Direct Download Link of any Telegram file</a>
#👉 <a href="#">Get a Telegram sticker as a Telegram downloadable media</a>
#👉 <a href="#">Generate Custom Thumbnail by sending two photos in a Media Album</a>
#👉 <a href="#">Upload as file from any HTTP link, with custom thumbnail support</a>
#👉 <a href="#">Convert To Streamable Video, any Telegram file</a>
#👉 <a href="#">Convert To Telegram Audio, the media sent as Telegram Documents</a>
#👉 <a href="#">ReName Telegram files, with custom thumbnail support</a>
#👉 <a href="#">Trim large videos</a>, and <a href="#">Take Screenshots</a> of Telegram media files.
#👉 <a href="#">Extract compressed Telegram media</a>
#👉 PLUS, all newly features that are going to be added in the feature*.
#-------
#NOTE: After payment you must take screenshot of receipt and send to the admin
#@DwayneJohnsonn """
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    NOYES_URL = "@GetPublicLinkBot URL detected. Please do not abuse the service!"
    DOWNLOAD_START = "Downloading"
    UPLOAD_START = "Uploading"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Please rate me if you find me useful. https://t.me/tlgrmcbot?start=mtuploader_bot-review"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nPlease rate me if you find me useful. https://t.me/tlgrmcbot?start=mtuploader_bot-review \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.org/DwayneJohnsonn'>@DwayneJohnsonn</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "something is wrong with the URL you gave me 🤦‍♀️. If you think this could be a bug please report on https://github.com/thwarikh/fmDL_Bot/issues OR https://telegram.org/thwarikh\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Current plan details
--------
Telegram ID: <code>{}</code>
Plan name: <a href='https://t.me/MT_MaptapMovies'>{}</a>
Expires on: {}"""
    HELP_USER = """There are multiple things I can do:
👉 <a href="#">All Supported Video Formats of https://rg3.github.io/youtube-dl/supportedsites.html, with custom file name and custom thumbnail support</a>
👉 <a href="#">Upload as file from any HTTP link, with custom thumbnail support</a>
👉 <a href="#">Convert To Streamable Video, any Telegram file</a>
👉 <a href="#">Convert To Telegram Audio, the media sent as Telegram Documents</a>
👉 <a href="#">ReName Telegram files, with custom thumbnail support</a>
👉 <a href="#">Get High Speed Direct Download Link of any Telegram file</a>
👉 <a href="#">Generate Custom Thumbnail by sending two photos in a Media Album</a>
👉 <a href="#">Trim large videos</a>, and <a href="#">Take Screenshots</a> of Telegram media files.
👉 <a href="#">Extract compressed Telegram media</a>
👉 <a href="#">Get a Telegram sticker as a Telegram downloadable media</a>
--------
Send /me to know current plan details"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n © @MTUploader_Bot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a HTTP link, to extract embedded subtitle"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please Contact @DwayneJohnsonn to remove this restriction."
    #FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to @DwayneJohnsonn"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per hour.
/upgrade or Try 3600 seconds later."""
    G_DRIVE_GIVE_URL_TO_LOGIN = "Please login using {}. Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_IN_VALID_FORMAT = "Send `/gsetup <YOUR CODE>`"
    G_DRIVE_SETUP_COMPLETE = "Logged In."
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users. "
