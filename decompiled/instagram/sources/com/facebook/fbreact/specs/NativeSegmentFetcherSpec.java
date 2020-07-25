package com.facebook.fbreact.specs;

import com.facebook.react.bridge.Callback;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;
import com.facebook.react.bridge.ReactModuleWithSpec;
import p000X.A44;
import p000X.C139155x8;
import p000X.C23043A0y;

public abstract class NativeSegmentFetcherSpec extends ReactContextBaseJavaModule implements ReactModuleWithSpec, C139155x8 {
    @ReactMethod
    public abstract void fetchSegment(double d, C23043A0y a0y, Callback callback);

    @ReactMethod
    public void getSegment(double d, C23043A0y a0y, Callback callback) {
    }

    public NativeSegmentFetcherSpec(A44 a44) {
        super(a44);
    }
}