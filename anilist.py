import discord
import requests
from discord.ext import commands
from discord.ext.commands import Cog

# import json



async def anime(ctx, desenio: str) -> str: 
    
    query = '''
    query ($id: Int, $page: Int, $perPage: Int, $search: String) {
        Page (page: $page, perPage: $perPage) {
            pageInfo {
                currentPage
                hasNextPage
                perPage
            }
            media (id: $id, search: $search, type: ANIME) {
                id
                title {
                    romaji
                }
            }
        }
    }
    '''

    variables = {
        'search': f"{desenio}",
        'page': 1,
        'perPage': 3
    }

    url = 'https://graphql.anilist.co'

    
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    
    anime_id = data['data']['Page']['media'][0]['id']
    anime_title = data['data']['Page']['media'][0]['title']['romaji']
    link = f"https://anilist.co/anime/{anime_id}/"
    await ctx.send(f"**{anime_title}**: {link}")

async def manga(ctx, desenio):
    query = '''
    query ($id: Int, $page: Int, $perPage: Int, $search: String) {
        Page (page: $page, perPage: $perPage) {
            pageInfo {
                currentPage
                hasNextPage
                perPage
            }
            media (id: $id, search: $search, type: MANGA) {
                id
                title {
                    romaji
                }
            }
        }
    }
    '''

    variables = {
        'search': f"{desenio}",
        'page': 1,
        'perPage': 3
    }

    url = 'https://graphql.anilist.co'

    
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    
    manga_id = data['data']['Page']['media'][0]['id']
    manga_title = data['data']['Page']['media'][0]['title']['romaji']
    link = f"https://anilist.co/manga/{manga_id}/"
    await ctx.send(f"**{manga_title}**: {link}")

async def user_profile(ctx, username: str):
    query = '''
    query ($name: String) {
      User(name: $name) {
        id
        name
        about
        avatar {
          large
        }
        siteUrl
      }
    }
    '''
    variables = {
        'name': username
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    data = response.json()
    user = data.get('data', {}).get('User')
    if not user:
        await ctx.send(f"Usuário '{username}' não encontrado.")
        return

    embed = discord.Embed(
        title=f"Perfil de {user['name']}",
        url=user['siteUrl'],
        description=user.get('about', 'Sem descrição disponível.'),
        color=0x2E51A2
    )
    embed.set_thumbnail(url=user['avatar']['large'])
    await ctx.send(embed=embed)