package dev.lukeharris.tasks;

import static android.view.View.OVER_SCROLL_NEVER;

import android.os.Bundle;

import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        bridge.getWebView().setOverScrollMode(OVER_SCROLL_NEVER);
    }
}
