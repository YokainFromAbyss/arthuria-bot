import asyncio

from bungio import Client
from bungio.models import BungieMembershipType, DestinyUser, DestinyRecordDefinition, DestinyActivityModeType,\
    DestinyActivityDefinition

# create the client obj with our bungie authentication
client = Client(
    bungie_client_id="1234",
    bungie_client_secret="1234",
    bungie_token="",
)


async def main():
    # create a user obj using a known bungie id
    # res = await client.manifest.fetch_all(manifest_class=DestinyActivityDefinition)
    # for activ in res:
    #     if 'Vault of Glass' in activ.display_properties.name:
    #         print(activ.hash)
    #         print(activ.display_properties.name)
    #         print(activ.display_properties.description)
    #         print(activ.activity_mode_types)
    # for tr in res:
    #     if 'Edge' in tr.display_properties.name or 'Edge' in tr.display_properties.description:
    #         print(tr.hash)
    #         print(tr.display_properties.name)
    #         print(tr.display_properties.description)
    # return
    userA = DestinyUser(membership_id=4611686018484705102, membership_type=BungieMembershipType.TIGER_STEAM)
    # userA = DestinyUser(membership_id=4611686018467794580, membership_type=BungieMembershipType.TIGER_STEAM)
    # iterate thought the raids that user has played
    # pr = await userA.get_membership_data_by_id()
    # lll = [100, 101, 102, 103, 104, 105, 200, 201, 202, 203, 204, 205, 206, 300, 301, 302, 303, 304, 305, 306, 307, 308,
    #        309, 310, 400, 401, 402, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
    # pri = await userA.get_profile(components=lll)
    # print(pri.profile_collectibles.data.collectibles)
    # for c in pri.characters.data.values():
    #     print(c.class_type)
    # print(pri.profile_records.data.active_score)
    # print(pri.profile_records.data.legacy_score)
    # for k, v in pri.profile_records.data.records.items():
    #     print(f'key {k}, value {v}')
    #     await v.fetch_manifest_information()
    #     print(v.to_dict())
    #     return
    async for activity in userA.yield_activity_history(mode=DestinyActivityModeType.RAID):
        if activity.activity_details.director_activity_hash == 3022541210 \
                or activity.activity_details.director_activity_hash == 3881495763:

            if activity.values["completed"].basic.value > 0 and activity.values["playerCount"].basic.value == 3:
                print("===activity_details===")
                print(activity.activity_details.to_dict())
                print("===period===")
                print(activity.period)
                print("===values===")
                for v in activity.values.values():
                    print(v.stat_id, ": ", v.basic.value)


# bungio is by nature asynchronous, it can only be run in an asynchronous context
asyncio.run(main())
