-- List all shows contained in `hbtn_0d_tvshows` DB
-- LEFT JOIN tv_show_genres on tv_shows on the common filed `show_id`
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
