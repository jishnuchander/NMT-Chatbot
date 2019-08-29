import os
package_path = ''

out_dir = os.path.join(package_path, "model/")

train_dir = os.path.join(package_path, "data/")

source_dir = os.path.join(package_path, "new_data/")

preprocessing = {
    'samples': -1,
    'vocab_size': 15000,
    'joined_vocab': True,
    'use_bpe': True,
    'embedded_detokenizer': True,
    'test_size': 100,
    'epochs': [0.001, 0.0001, 0.00001],
    'cache_preparation': False,
    'source_folder': source_dir,
    'train_folder': train_dir,
    'protected_phrases_standard_file': os.path.join(package_path, 'setup/protected_phrases_standard.txt'),
    'protected_phrases_bpe_file': os.path.join(package_path, 'setup/protected_phrases_bpe.txt'),
    'answers_detokenize_file': os.path.join(package_path, 'setup/answers_detokenize.txt'),
    'answers_replace_file': os.path.join(package_path, 'setup/answers_replace.txt'),
    'cpu_count': None,
}

#hparams
hparams = {
    'attention': 'scaled_luong',
    'num_train_steps': 10000000,
    'num_layers': 2,
    'num_units': 512,
    'optimizer': 'adam',
    'encoder_type': 'bi',
    'learning_rate': 0.001,
    'beam_width': 20,
    'length_penalty_weight': 1.0,
    'num_translations_per_input': 20,
    'src': 'from',
    'tgt': 'to',
    'vocab_prefix': os.path.join(train_dir, "vocab"),
    'train_prefix': os.path.join(train_dir, "train"),
    'dev_prefix': os.path.join(train_dir, "tst2012"),
    'test_prefix': os.path.join(train_dir, "tst2013"),
    'out_dir': out_dir,
    'share_vocab': preprocessing['joined_vocab'],
}

# response score settings
score = {
    'use_scoring': True,
    'answers_subsentence_score_file': os.path.join(package_path, 'setup/answers_subsentence_score.txt'),
    'starting_score': 10,
    'pick_random': 'best_score',
    'bad_response_threshold': 0,
    'question_answer_similarity_threshold': 0.75,
    'question_answer_similarity_sentence_len': 10,
    'question_answer_similarity_modifier': 'value',  # 'multiplier'
    'question_answer_similarity_modifier_value': -100,
    'subsentence_dividers': "[\.,!\?;]|but",
    'answer_subsentence_similarity_threshold': 0.5,
    'answer_subsentence_similarity_sentence_len': 10,
    'answer_subsentence_similarity_modifier': 'multiplier',  # 'value'
    'answer_subsentence_similarity_modifier_value': -10,
    'url_delimiters': ' )',
    'incorrect_url_modifier_value': -100,
    'sentence_ending': '[\.!\?;]|FTFY',
    'sentence_ending_sentence_len': 20,
    'no_ending_modifier_value': (-100, -5),
    'unk_modifier_value': -100,
    'use_subsentence_score': True,
    'position_modifier': {1: 1.5, 2: 1, 4: 0.5, 8: 0},
    'ascii_emoticon_non_char_to_all_chars_ratio': 0.7,
    'ascii_emoticon_modifier_value': 1,
    'reward_long_sentence_value': 0.15,
    'show_score_modifiers': False,
}

######## DO NOT CHANGE ANYTHING BELOW ########

if preprocessing['use_bpe']:
    preprocessing['embedded_detokenizer'] = True
    hparams['subword_option'] = 'spm'

preprocessing['protected_phrases_file'] = preprocessing['protected_phrases_bpe_file'] if preprocessing['use_bpe'] else preprocessing['protected_phrases_standard_file']

if preprocessing['use_bpe']:
    hparams['vocab_prefix'] += '.bpe'
    hparams['train_prefix'] += '.bpe'
    hparams['dev_prefix'] += '.bpe'
    hparams['test_prefix'] += '.bpe'

if preprocessing['joined_vocab']:
    hparams['share_vocab'] = True

if not score['use_scoring']:
    score['bad_response_threshold'] = 0
