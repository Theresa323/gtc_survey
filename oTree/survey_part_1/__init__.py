from otree.api import *


doc = 'survey_part_1_exp'


class C(BaseConstants):
    NAME_IN_URL = 'demo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.IntegerField(
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
        ],
        label='What best describes your gender?'
    )

    year_of_birth = models.IntegerField(
        min=1922, max=2022, 
        label='What is your year of birth? ')

    nationality = models.IntegerField(
        choices=[
            [0, 'Afghanistan'], [1, 'Åland Islands'], [2, 'Albania'], [3, 'Algeria'], [4, 'American Samoa'], [5, 'Andorra'], [6, 'Angola'], [7, 'Anguilla'], [8, 'Antarctica'], [9, 'Antigua and Barbuda'], [10, 'Argentina'], [11, 'Armenia'], [12, 'Aruba'], [13, 'Australia'], [14, 'Austria'], [15, 'Azerbaijan'], [16, 'Bahamas'], [17, 'Bahrain'], [18, 'Bangladesh'], [19, 'Barbados'], [20, 'Belarus'], [21, 'Belgium'], [22, 'Belize'], [23, 'Benin'], [24, 'Bermuda'], [25, 'Bhutan'], [26, 'Bolivia (Plurinational State of)'], [27, 'Bonaire, Sint Eustatius and Saba'], [28, 'Bosnia and Herzegovina'], [29, 'Botswana'], [30, 'Bouvet Island'], [31, 'Brazil'], [32, 'British Indian Ocean Territory'], [33, 'British Virgin Islands'], [34, 'Brunei Darussalam'], [35, 'Bulgaria'], [36, 'Burkina Faso'], [37, 'Burundi'], [38, 'Cabo Verde'], [39, 'Cambodia'], [40, 'Cameroon'], [41, 'Canada'], [42, 'Cayman Islands'], [43, 'Central African Republic'], [44, 'Chad'], [45, 'Chile'], [46, 'China'], [47, 'China, Hong Kong Special Administrative Region'], [48, 'China, Macao Special Administrative Region'], [49, 'Christmas Island'], [50, 'Cocos (Keeling) Islands'], [51, 'Colombia'], [52, 'Comoros'], [53, 'Congo'], [54, 'Cook Islands'], [55, 'Costa Rica'], [56, 'Côte d’Ivoire'], [57, 'Croatia'], [58, 'Cuba'], [59, 'Curaçao'], [60, 'Cyprus'], [61, 'Czechia'], [62, "Democratic People's Republic of Korea"], [63, 'Democratic Republic of the Congo'], [64, 'Denmark'], [65, 'Djibouti'], [66, 'Dominica'], [67, 'Dominican Republic'], [68, 'Ecuador'], [69, 'Egypt'], [70, 'El Salvador'], [71, 'Equatorial Guinea'], [72, 'Eritrea'], [73, 'Estonia'], [74, 'Eswatini'], [75, 'Ethiopia'], [76, 'Falkland Islands (Malvinas)'], [77, 'Faroe Islands'], [78, 'Fiji'], [79, 'Finland'], [80, 'France'], [81, 'French Guiana'], [82, 'French Polynesia'], [83, 'French Southern Territories'], [84, 'Gabon'], [85, 'Gambia'], [86, 'Georgia'], [87, 'Germany'], [88, 'Ghana'], [89, 'Gibraltar'], [90, 'Greece'], [91, 'Greenland'], [92, 'Grenada'], [93, 'Guadeloupe'], [94, 'Guam'], [95, 'Guatemala'], [96, 'Guernsey'], [97, 'Guinea'], [98, 'Guinea-Bissau'], [99, 'Guyana'], [100, 'Haiti'], [101, 'Heard Island and McDonald Islands'], [102, 'Holy See'], [103, 'Honduras'], [104, 'Hungary'], [105, 'Iceland'], [106, 'India'], [107, 'Indonesia'], [108, 'Iran (Islamic Republic of)'], [109, 'Iraq'], [110, 'Ireland'], [111, 'Isle of Man'], [112, 'Israel'], [113, 'Italy'], [114, 'Jamaica'], [115, 'Japan'], [116, 'Jersey'], [117, 'Jordan'], [118, 'Kazakhstan'], [119, 'Kenya'], [120, 'Kiribati'], [121, 'Kuwait'], [122, 'Kyrgyzstan'], [123, "Lao People's Democratic Republic"], [124, 'Latvia'], [125, 'Lebanon'], [126, 'Lesotho'], [127, 'Liberia'], [128, 'Libya'], [129, 'Liechtenstein'], [130, 'Lithuania'], [131, 'Luxembourg'], [132, 'Madagascar'], [133, 'Malawi'], [134, 'Malaysia'], [135, 'Maldives'], [136, 'Mali'], [137, 'Malta'], [138, 'Marshall Islands'], [139, 'Martinique'], [140, 'Mauritania'], [141, 'Mauritius'], [142, 'Mayotte'], [143, 'Mexico'], [144, 'Micronesia (Federated States of)'], [145, 'Monaco'], [146, 'Mongolia'], [147, 'Montenegro'], [148, 'Montserrat'], [149, 'Morocco'], [150, 'Mozambique'], [151, 'Myanmar'], [152, 'Namibia'], [153, 'Nauru'], [154, 'Nepal'], [155, 'Netherlands'], [156, 'New Caledonia'], [157, 'New Zealand'], [158, 'Nicaragua'], [159, 'Niger'], [160, 'Nigeria'], [161, 'Niue'], [162, 'Norfolk Island'], [163, 'North Macedonia'], [164, 'Northern Mariana Islands'], [165, 'Norway'], [166, 'Oman'], [167, 'Pakistan'], [168, 'Palau'], [169, 'Panama'], [170, 'Papua New Guinea'], [171, 'Paraguay'], [172, 'Peru'], [173, 'Philippines'], [174, 'Pitcairn'], [175, 'Poland'], [176, 'Portugal'], [177, 'Puerto Rico'], [178, 'Qatar'], [179, 'Republic of Korea'], [180, 'Republic of Moldova'], [181, 'Réunion'], [182, 'Romania'], [183, 'Russian Federation'], [184, 'Rwanda'], [185, 'Saint Barthélemy'], [186, 'Saint Helena'], [187, 'Saint Kitts and Nevis'], [188, 'Saint Lucia'], [189, 'Saint Martin (French Part)'], [190, 'Saint Pierre and Miquelon'], [191, 'Saint Vincent and the Grenadines'], [192, 'Samoa'], [193, 'San Marino'], [194, 'Sao Tome and Principe'], [195, 'Sark'], [196, 'Saudi Arabia'], [197, 'Senegal'], [198, 'Serbia'], [199, 'Seychelles'], [200, 'Sierra Leone'], [201, 'Singapore'], [202, 'Sint Maarten (Dutch part)'], [203, 'Slovakia'], [204, 'Slovenia'], [205, 'Solomon Islands'], [206, 'Somalia'], [207, 'South Africa'], [208, 'South Georgia and the South Sandwich Islands'], [209, 'South Sudan'], [210, 'Spain'], [211, 'Sri Lanka'], [212, 'State of Palestine'], [213, 'Sudan'], [214, 'Suriname'], [215, 'Svalbard and Jan Mayen Islands'], [216, 'Sweden'], [217, 'Switzerland'], [218, 'Syrian Arab Republic'], [219, 'Tajikistan'], [220, 'Thailand'], [221, 'Timor-Leste'], [222, 'Togo'], [223, 'Tokelau'], [224, 'Tonga'], [225, 'Trinidad and Tobago'], [226, 'Tunisia'], [227, 'Turkey'], [228, 'Turkmenistan'], [229, 'Turks and Caicos Islands'], [230, 'Tuvalu'], [231, 'Uganda'], [232, 'Ukraine'], [233, 'United Arab Emirates'], [234, 'United Kingdom of Great Britain and Northern Ireland'], [235, 'United Republic of Tanzania'], [236, 'United States Minor Outlying Islands'], [237, 'United States of America'], [238, 'United States Virgin Islands'], [239, 'Uruguay'], [240, 'Uzbekistan'], [241, 'Vanuatu'], [242, 'Venezuela (Bolivarian Republic of)'], [243, 'Viet Nam'], [244, 'Wallis and Futuna Islands'], [245, 'Western Sahara'], [246, 'Yemen'], [247, 'Zambia'], [248, 'Zimbabwe']
        ],
        label='What is your nationality?'
    )

    education = models.IntegerField(
        choices=[
            [1, 'High School'],
            [2, 'Undergraduate Studies'],
            [3, 'Graduate Studies'],
            [4, 'Post-Graduate Studies'],
            [5, 'Other'],
            [6, 'Prefer not to say'],
        ],
        label='What is the highest degree of education you have completed?'
    )

    been_to_germany = models.BooleanField(
        choices=[[True, 'Yes'],[False, 'No'],],
        label='Have you ever been to Germany?'
    )
    been_to_israel = models.BooleanField(
        choices=[[True, 'Yes'],[False, 'No'],],
        label='Have you ever been to Israel?'
    )


# PAGES
class Introduction(Page):
    pass

class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'year_of_birth', 'nationality', 'education', 'been_to_germany', 'been_to_israel']
    '''
    @staticmethod
    def error_message(player, values):
        if (values['been_to_germany'] == False and (values['been_to_berlin'] == True or values['been_to_hamburg'] == True)) or (values['been_to_israel'] == False and (values['been_to_jerusalem'] == True or values['been_to_telaviv'] == True)):
            return 'Invalid Input'
    '''
        

page_sequence = [Introduction, Demographics]
