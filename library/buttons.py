from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


home_button = [
    [
        InlineKeyboardButton("π Source", "source_btn"),
        InlineKeyboardButton("β¬οΈ  Fr. Id", "from_btn"),
        InlineKeyboardButton("β Help", url="https://bit.ly/3z2jquF"),
    ],
    [
        InlineKeyboardButton("π― Target", "target_btn"),
        InlineKeyboardButton("β¬οΈ  To Id", "up_to_btn"),
        InlineKeyboardButton("Types  β‘", "types_btn"),
    ],
    [
        InlineKeyboardButton("Delayed", "delay_btn"),
        InlineKeyboardButton("Caption", "caption_btn"),
        InlineKeyboardButton("FNAC", "f_caption_btn"),
    ],
    [
        InlineKeyboardButton("ποΈ  View", "view_btn"),
        InlineKeyboardButton("βοΈ CC", "cust_captn_btn"),
        InlineKeyboardButton("β  Close", "close_btn"),
    ],
    [
        InlineKeyboardButton("π  Reset", "rst_btn"),
        InlineKeyboardButton("π  Restart", "restart_btn"),
    ],
    [InlineKeyboardButton("π¦ Clone Messages π¦", "clone_btn")],
]


start_button = [
    [
        InlineKeyboardButton("π GitHub π", url="github.com/m4mallu/clonebot"),
        InlineKeyboardButton("βοΈSettings β", "start_btn"),
    ]
]


types_button = [
    [
        InlineKeyboardButton("Docs β", "docs_yes_btn"),
        InlineKeyboardButton("Video β", "video_yes_btn"),
        InlineKeyboardButton("Audio β", "audio_yes_btn"),
    ],
    [
        InlineKeyboardButton("Photo β", "photo_yes_btn"),
        InlineKeyboardButton("Voice β", "voice_yes_btn"),
        InlineKeyboardButton("Text β", "text_yes_btn"),
    ],
    [
        InlineKeyboardButton("βοΈ View", "view_types"),
        InlineKeyboardButton("β¬οΈ Back", "start_btn"),
    ],
]


stop_button = [[InlineKeyboardButton("π« STOP π«", "stop_clone")]]


finished_button = [
    [
        InlineKeyboardButton("Home", "start_btn"),
        InlineKeyboardButton("Close", "close_btn"),
    ]
]


close_button = [
    [
        InlineKeyboardButton("Delete", "close_btn"),
        InlineKeyboardButton("Close", "clear_btn"),
    ]
]


terminate_btn = [
    [
        InlineKeyboardButton("π§Έ Updates", url="https://github.com/m4mallu/clonebot"),
        InlineKeyboardButton("β Usage", url="https://bit.ly/3z2jquF"),
    ],
    [
        InlineKeyboardButton("π« Terminate", "terminate_btn"),
        InlineKeyboardButton("π  Home", "start_btn"),
    ],
]


indexing_skip_button = [[InlineKeyboardButton("πΉ Skip", "index_skip_btn")]]


purging_skip_button = [[InlineKeyboardButton("πΉ Skip", "purge_skip_btn")]]


purge_button = [
    [
        InlineKeyboardButton("Nop", "purge_no_btn"),
        InlineKeyboardButton("Purge it π", "purge_yes_btn"),
    ]
]

caption_cnf_button = [
    [
        InlineKeyboardButton("YES β", "capt_cnf_yes_btn"),
        InlineKeyboardButton("NO β", "capt_cnf_no_btn"),
    ]
]


reply_markup_purge = InlineKeyboardMarkup(purge_button)

reply_markup_skip_index = InlineKeyboardMarkup(indexing_skip_button)

reply_markup_skip_purge = InlineKeyboardMarkup(purging_skip_button)

reply_markup_stop = InlineKeyboardMarkup(stop_button)

reply_markup_home = InlineKeyboardMarkup(home_button)

reply_markup_start = InlineKeyboardMarkup(start_button)

reply_markup_terminate = InlineKeyboardMarkup(terminate_btn)

reply_markup_finished = InlineKeyboardMarkup(finished_button)

reply_markup_types_button = InlineKeyboardMarkup(types_button)

reply_markup_close = InlineKeyboardMarkup(close_button)

reply_markup_cap_cnf = InlineKeyboardMarkup(caption_cnf_button)
