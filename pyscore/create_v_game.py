import sqlite3
import os

con = sqlite3.connect(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "db.sqlite3")
)
cur = con.cursor()

cur.execute("DROP VIEW v_game")
cur.execute(
    # 기존 'CREATE VIEW v_game AS SELECT pyhome_gamelist.id AS id, pyhome_gamelist.gamedate AS gamedate, pyhome_gamelist.gamememo AS gamememo, GROUP_CONCAT(auth_user.username, ",") AS names, SUM(pyhome_score.coupon) AS coupon, COUNT(pyhome_score.id) AS count FROM pyhome_gamelist LEFT JOIN pyhome_score ON pyhome_score.foreignkey_id = pyhome_gamelist.id LEFT JOIN auth_user ON auth_user.id = pyhome_score.username_id GROUP BY pyhome_gamelist.id'
    # id값이숫자로만불러와짐 'CREATE VIEW v_game AS SELECT pyhome_gamelist.id AS id, pyhome_gamelist.gamedate AS gamedate,               pyhome_gamelist.part_id AS part,             pyhome_gamelist.gamememo AS gamememo, GROUP_CONCAT(auth_user.username, ",") AS names, SUM(pyhome_score.coupon) AS coupon, COUNT(pyhome_score.id) AS count FROM pyhome_gamelist LEFT JOIN pyhome_score ON pyhome_score.foreignkey_id = pyhome_gamelist.id LEFT JOIN auth_user ON auth_user.id = pyhome_score.username_id GROUP BY pyhome_gamelist.id'
    'CREATE VIEW v_game AS SELECT pyhome_gamelist.id AS id, pyhome_gamelist.gamedate AS gamedate,              pyhome_gamelist.part_id AS part,             pyhome_gamelist.gamememo AS gamememo, GROUP_CONCAT(auth_user.username, ",") AS names, SUM(pyhome_score.coupon) AS coupon, COUNT(pyhome_score.id) AS count FROM pyhome_gamelist LEFT JOIN pyhome_score ON pyhome_score.foreignkey_id = pyhome_gamelist.id LEFT JOIN auth_user ON auth_user.id = pyhome_score.username_id GROUP BY pyhome_gamelist.id'
)

# pyhome_gamelist.part_id AS part,
# LEFT JOIN auth_user ON auth_user.id = pyhome_score.username_id

# pyhome_gamelist.part_id AS part LEFT JOIN auth_user ON auth_user.id = pyhome_score.username_id,

con.commit()
