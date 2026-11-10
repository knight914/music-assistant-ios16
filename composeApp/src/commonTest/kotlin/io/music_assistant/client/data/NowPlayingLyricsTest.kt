package io.music_assistant.client.data

import io.music_assistant.client.data.model.client.LrcLine
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertNull

class NowPlayingLyricsTest {
    private val lines = listOf(
        LrcLine(1000, "第一句"),
        LrcLine(2000, "  "),
        LrcLine(3000, "第二句"),
    )

    @Test fun introAndBlankRestoreOriginalTitle() {
        assertNull(syncedLyricAt(lines, 0.0))
        assertNull(syncedLyricAt(lines, 2.5))
        assertNull(syncedLyricAt(emptyList(), 10.0))
    }

    @Test fun exactBoundaryAndSeekingBothDirections() {
        assertEquals("第一句", syncedLyricAt(lines, 1.0))
        assertEquals("第二句", syncedLyricAt(lines, 3.0))
        assertEquals("第一句", syncedLyricAt(lines, 1.5))
        assertNull(syncedLyricAt(lines, 0.5))
    }
}
