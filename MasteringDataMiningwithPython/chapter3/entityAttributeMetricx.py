import sys
import pymysql
from nltk.metrics import edit_distance

from soundex import soundex



db = pymysql.connect(host='localhost', db='rfrg', user='root', passwd='45668668', port=3306, charset='utf8mb4', autocommit=True)
cursor = db.cursor()

# get all projects with matching URLs
cursor.execute("""TRUNCATE TABLE book_entity_matches""")
cursor.execute("""INSERT INTO book_entity_matches (
                  rf_project_name, rg_project_name)
                  SELECT rf.project_name, rg.project_name
                  FROM rfrg.book_rf_entities rf
                  INNER JOIN rfrg.book_rg_entities rg
                  ON rf.url = rg.url""")

# get projects that have matching project names
cursor.execute("""INSERT INTO book_entity_matches (
                  rf_project_name, rg_project_name)
                  SELECT rf.project_name, rg.project_name
                  FROM rfrg.book_rf_entities rf
                  INNER JOIN book_rg_entities rg
                  ON rf.project_name = rg.project_name
                  WHERE rf.project_name NOT IN (
                      SELECT bem.rf_project_name
                      FROM book_entity_matches bem)""")

cursor.execute("""SELECT bem.rf_project_name, bem.rg_project_name, rfe.url, rfe.url
                  FROM rfrg.book_entity_matches bem
                  INNER JOIN rfrg.book_rg_entities rge
                  ON bem.rg_project_name = rge.project_name
                  INNER JOIN rfrg.book_rf_entities rfe
                  ON bem.rf_project_name = rfe.project_name
                  ORDER BY bem.rf_project_name""")
projectPairs = cursor.fetchall()


for (projectPair) in projectPairs:
    RFname = projectPair[0]
    RGname = projectPair[1]
    RFurl = projectPair[2]
    RGurl = projectPair[3]

    # lowercase everything
    RFnameLC = RFname.lower()
    RGnameLC = RGname.lower()
    RFurlLC = RFurl.lower()
    RGurlLC = RGurl.lower()


    levNames = edit_distance(RFnameLC, RGnameLC)
    levURLs = edit_distance(RFurlLC, RGurlLC)
    soundexRFname = soundex(RFnameLC)
    soundexRGname = soundex(RGnameLC)

    # is the RF project_name inside the RG project name?
    if RFnameLC in RGnameLC:
        rf_in_rg = 1
    else:
        rf_in_rg = 0

    # is the RF project_name inside the RG project URL?
    if RFnameLC in RGurl:
        rf_in_rgurl = 1
    else:
        rf_in_rgurl = 0


    # do RF devs match the RG devs?
    cursor.execute("""SELECT rf.dev_username, rf.dev_realname
                      FROM rfrg.book_rf_entity_people rf
                      WHERE rf.project_name = %s
                      AND (rf.dev_username IN (
                          SELECT rg.person_name
                          FROM rfrg.book_rg_entity_people rg
                          WHERE rg.project_name = %s)
                          OR rf.dev_realname IN (
                          SELECT rg.person_name
                          FROM rfrg.book_rg_entity_people rg
                          WHERE rg.project_name = %s))""",
                          (RFname, RGname, RGname))

    result = cursor.fetchone()
    if result is not None:
        rfdev_in_rgdev = 1
    else:
        rfdev_in_rgdev = 0


    cursor.execute("UPDATE book_entity_matches \
                      SET rf_name_soundex = %s, \
                          rg_name_soundex = %s, \
                          url_levenshtein = %s, \
                          name_levenshtein = %s, \
                          rf_name_in_rg_name = %s, \
                          rf_name_in_rg_url = %s, \
                          rf_dev_in_rg_dev = %s \
                      WHERE rf_project_name = %s \
                      AND rg_project_name = %s", 
                      (soundexRFname, soundexRGname, levURLs, levNames, rf_in_rg, rf_in_rgurl, rfdev_in_rgdev, RFname, RGname))

db.close()
