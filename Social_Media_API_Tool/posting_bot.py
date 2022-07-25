from ayrshare import SocialPost
social = SocialPost('XXXXXXXXXXXXXXXXX')

postResponse = social.post({
    'post':'This message was posted using #Ayrshare Social Post #API and #Python #100DaysOfCode',
    'platforms': ['twitter', 'facebook'],
    'title': 'Test post',
})