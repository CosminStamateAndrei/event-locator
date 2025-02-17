import discord

class EventPaginator(discord.ui.View):
    def __init__(self, events: list, author: discord.User):
        super().__init__(timeout=180)
        self.events = events
        self.author = author
        self.current_page = 0
        self.max_page = (len(events) - 1) // 5

    def get_current_page_embed(self) -> discord.Embed:
        start = self.current_page * 5
        end = start + 5
        page_events = self.events[start:end]
        embed = discord.Embed(
            title=f"Events (Page {self.current_page+1}/{self.max_page+1})",
            color=discord.Color.blue()
        )
        if not page_events:
            embed.description = "No events to display."
        else:
            for i, event in enumerate(page_events, start=1):
                name = event.get("name", "No name")
                date = event.get("dates", {}).get("start", {}).get("localDate", "No date")
                embed.add_field(name=f"{i}. {name}", value=f"Date: {date}", inline=False)
        return embed

    async def update_message(self, interaction: discord.Interaction):
        self.previous_button.disabled = (self.current_page == 0)
        self.next_button.disabled = (self.current_page == self.max_page)
        embed = self.get_current_page_embed()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="◀", style=discord.ButtonStyle.primary)
    async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.author:
            await interaction.response.send_message("This is not your command.", ephemeral=True)
            return
        if self.current_page > 0:
            self.current_page -= 1
        await self.update_message(interaction)

    @discord.ui.button(label="▶", style=discord.ButtonStyle.primary)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.author:
            await interaction.response.send_message("This is not your command.", ephemeral=True)
            return
        if self.current_page < self.max_page:
            self.current_page += 1
        await self.update_message(interaction)

    # Numbered buttons for each event slot in the page (1-5)
    @discord.ui.button(label="1", style=discord.ButtonStyle.secondary, row=1)
    async def button_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_event_button(interaction, 0)

    @discord.ui.button(label="2", style=discord.ButtonStyle.secondary, row=1)
    async def button_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_event_button(interaction, 1)

    @discord.ui.button(label="3", style=discord.ButtonStyle.secondary, row=1)
    async def button_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_event_button(interaction, 2)

    @discord.ui.button(label="4", style=discord.ButtonStyle.secondary, row=1)
    async def button_4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_event_button(interaction, 3)

    @discord.ui.button(label="5", style=discord.ButtonStyle.secondary, row=1)
    async def button_5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_event_button(interaction, 4)

    async def handle_event_button(self, interaction: discord.Interaction, index: int):
        if interaction.user != self.author:
            await interaction.response.send_message("This is not your command.", ephemeral=True)
            return
        event_index = self.current_page * 5 + index
        if event_index >= len(self.events):
            await interaction.response.send_message("No event in this slot.", ephemeral=True)
            return
        event = self.events[event_index]
        url = event.get("url", "No URL")
        await interaction.response.send_message(f"Event link: {url}", ephemeral=True)