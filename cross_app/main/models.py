from django.db import models
from django.db import connection, transaction

class Match_info(models.Model): # TODO:(murat) Bunu test icin yazmistin, degistir.
    match_id = models.PositiveIntegerField()

class TfMatch(models.Model):
    match_id = models.IntegerField(primary_key=True, db_column='MATCH_ID') # Field name made lowercase.
    home_team_id = models.IntegerField(db_column='HOME_TEAM_ID') # Field name made lowercase.
    visitor_team_id = models.IntegerField(db_column='VISITOR_TEAM_ID') # Field name made lowercase.
    match_date = models.CharField(max_length=33, db_column='MATCH_DATE', blank=True) # Field name made lowercase.
    match_time = models.CharField(max_length=15, db_column='MATCH_TIME', blank=True) # Field name made lowercase.
    match_stadium_id = models.IntegerField(null=True, db_column='MATCH_STADIUM_ID', blank=True) # Field name made lowercase.
    match_season_id = models.IntegerField(db_column='MATCH_SEASON_ID') # Field name made lowercase.
    match_league_id = models.IntegerField(db_column='MATCH_LEAGUE_ID') # Field name made lowercase.
    match_played_flag = models.CharField(max_length=3, db_column='MATCH_PLAYED_FLAG', blank=True) # Field name made lowercase.
    match_week = models.CharField(max_length=30, db_column='MATCH_WEEK', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tf_match'

class TdTeam(models.Model):
    team_id = models.IntegerField(primary_key=True, db_column='TEAM_ID') # Field name made lowercase.
    team_name = models.CharField(max_length=135, db_column='TEAM_NAME') # Field name made lowercase.
    team_foundation_year = models.CharField(max_length=12, db_column='TEAM_FOUNDATION_YEAR', blank=True) # Field name made lowercase.
    user_id = models.CharField(max_length=12, db_column='USER_ID', blank=True) # Field name made lowercase.
    team_type = models.IntegerField(null=True, db_column='TEAM_TYPE', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'td_team'
#    def getAggregateData(self):
#        # TODO: (caner) return a dict with the tabular data of the player

    def getHistoryTotal(self, matchCount):
        # Not sorted!
        matches = self.getLastNMatch(matchCount)
        distances = dict()
        for match in matches:
            distances[match[0]] = [match[1], self.getDistance(match[0], 1)]
        return distances

    def getHistoryHI(self, matchCount):
        # Not sorted!
        matches = self.getLastNMatch(matchCount)
        distances = dict()
        for match in matches:
            distances[match[0]] = [match[1], self.getDistance(match[0], 2)]
        return distances

    def getHistorySprint(self, matchCount):
        # not sorted
        matches = self.getLastNMatch(matchCount)
        distances = dict()
        for match in matches:
            distances[match[0]] = [match[1], self.getDistance(match[0], 3)]
        return distances

#    def getRadarMetrics(self):
#        # TODO

    def getLastNMatch(self, matchCount):
        # assumes no matches on same date
        cursor = connection.cursor()
        cursor.execute("""
                        select match_id, match_date from tf_match
                            where home_team_id = {0} or visitor_team_id = {0}
                            order by match_date desc
                            limit {1}
                        """.format(self.team_id, matchCount))
        rows = cursor.fetchall()
        return rows


    def getDistance(self, matchId, type):
        cursor = connection.cursor()
        if type == 1: #total distances
            cursor.execute("select sum(distance) from tf_match_stats_processed"
                           "  where match_id = {0}"
                           "    and team_id = {1}".format(matchId, self.team_id ))
        elif type == 2: # HIR
            cursor.execute("select sum(distance) from tf_match_stats_processed"
                           "  where match_id = {0}"
                           "    and move_category in (4,5)"
                           "    and team_id = {1}".format(matchId, self.team_id ))
        elif type == 3: #sprint
            cursor.execute("select sum(distance) from tf_match_stats_processed"
                           "  where match_id = {0}"
                           "    and move_category = 5"
                           "    and team_id = {1}".format(matchId, self.team_id ))
        else:
            return None
        row = cursor.fetchone()
        return row[0]

class TdPlayer(models.Model):
    player_id = models.IntegerField(primary_key=True, db_column='PLAYER_ID') # Field name made lowercase.
    player_name = models.CharField(max_length=1536, db_column='PLAYER_NAME', blank=True) # Field name made lowercase.
    player_surname = models.CharField(max_length=384, db_column='PLAYER_SURNAME', blank=True) # Field name made lowercase.
    player_full_name = models.CharField(max_length=1536, db_column='PLAYER_FULL_NAME', blank=True) # Field name made lowercase.
    player_birthdate = models.CharField(max_length=135, db_column='PLAYER_BIRTHDATE', blank=True) # Field name made lowercase.
    player_weight = models.IntegerField(null=True, db_column='PLAYER_WEIGHT', blank=True) # Field name made lowercase.
    player_height = models.IntegerField(null=True, db_column='PLAYER_HEIGHT', blank=True) # Field name made lowercase.
    player_birth_place = models.CharField(max_length=384, db_column='PLAYER_BIRTH_PLACE', blank=True) # Field name made lowercase.
    user_id = models.IntegerField(null=True, db_column='USER_ID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'td_player'

#    def getAggregateData(self):
#        info = dict()
#        return info

    def getHistoryTotal(self, matchCount):
        # Not sorted!
        matches = self.getLastNMatch(matchCount)
        distances = dict()
        for match in matches:
            distances[match[0]] = [match[1], self.getDistance(match[0], 1)]
        return distances

    def getHistoryHI(self, matchCount):
        # Not sorted!
        matches = self.getLastNMatch(matchCount)
        distances = dict()
        for match in matches:
            distances[match[0]] = [match[1], self.getDistance(match[0], 2)]
        return distances

    def getHistorySprint(self, matchCount):
        # not sorted
        matches = self.getLastNMatch(matchCount)
        distances = dict()
        for match in matches:
            distances[match[0]] = [match[1], self.getDistance(match[0], 3)]
        return distances

#    def getRadarMetrics(self):
#        # TODO

    def getJerseyNumber(self, match_id):
        cursor = connection.cursor()
        cursor.execute(("\n"
                        "            select jersey_number, team_id from vw_match_roster\n"
                        "                where match_id = {0}\n"
                        "                    and player_id = {1};\n"
                        "            "
            ).format(match_id, self.player_id))
        row = cursor.fetchone()
        return row

    def getLastNMatch(self, matchCount):
        # assumes no matches on same date
        cursor = connection.cursor()
        cursor.execute("""
                        select MATCH_ID, MATCH_DATE from vw_match_roster
                            where PLAYER_ID = {0}
                            order by MATCH_DATE desc
                            limit {1}
                        """.format(self.player_id, matchCount))
        rows = cursor.fetchall()
        return rows

    def getDistance(self, matchId, type):
        cursor = connection.cursor()
        if type == 1: #total distances
            cursor.execute("select sum(distance) from tf_match_stats_processed"
                           "  where match_id = {0}"
                           "    and team_id = {1}"
                           "    and jersey_number = {2}".format(matchId, self.getJerseyNumber(matchId)[1],self.getJerseyNumber(matchId)[0] ))
        elif type == 2: # HIR
            cursor.execute("select sum(distance) from tf_match_stats_processed"
                           "  where match_id = {0}"
                           "    and team_id = {1}"
                           "    and move_category in (4,5)"
                           "    and jersey_number = {2}".format(matchId, self.getJerseyNumber(matchId)[1],self.getJerseyNumber(matchId)[0] ))
        elif type == 3: #sprint
            cursor.execute("select sum(distance) from tf_match_stats_processed"
                           "  where match_id = {0}"
                           "    and team_id = {1}"
                           "    and move_category = 5"
                           "    and jersey_number = {2}".format(matchId, self.getJerseyNumber(matchId)[1],self.getJerseyNumber(matchId)[0] ))
        else:
            return None
        row = cursor.fetchone()
        return row[0]
