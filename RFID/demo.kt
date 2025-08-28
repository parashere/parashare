package com.example.app

import kotlinx.coroutines.*
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

package com.example.app

import kotlinx.coroutines.*
import kotlinx.coroutines.flow.MutableStateFlow

object InactivityManager {
    private val scope = CoroutineScope(Dispatchers.Main)
    private var job: Job? = null

    fun onUserAction() {
        viable.value = false   
        job?.cancel()
        job = scope.launch {
            delay(2000)       
            viable.value = true
        }
    }
}

/*入力側に
.previewKeyEvent { event ->
                if (event.type == KeyEventType.KeyDown) {
                    InactivityManager.onUserAction()
                }
                false


            }*/
